import random
import time
import sys
from collections import deque

def make_maze(n):
    maze = [[0]*n for _ in range(n)]

    for i in range(1, n-1, 2):
        random_number = random.randint(0, n-1)
        for j in range(n):
            if j != random_number:
                maze[i][j] = 1

    return maze

def find_path(x, y):
    global Q
    global cnt
    global maze
    visited = [[0]*n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    stack = []
    Q = deque()
    cnt = 0
    now = (x, y)

    stack.append(now)
    maze[now[1]][now[0]] = 2
    print(f"------------탈출 시작!--------------")
    for i in range(n):
        print(maze[i])
    maze[now[1]][now[0]] = 0
    visited[now[1]][now[0]] = 1
    print()
    Q.append(now)

    while now[0]!=n-1 or now[1]!=n-1:
        cnt+=1
        for i in range(4):
            next_x = now[0]+dx[i]
            next_y = now[1]+dy[i]
            if 0<=next_x<=n-1 and 0<=next_y<=n-1:
                if visited[next_y][next_x] == 0 and maze[next_y][next_x]==0:
                    now = (next_x, next_y)
                    stack.append((next_x, next_y))
                    visited[next_y][next_x] = 1
                    break
        else:
            now = stack.pop()

        maze[now[1]][now[0]]=2
        print(f"{cnt}번째 이동입니다")
        for i in range(n):
            print(maze[i])
        maze[now[1]][now[0]]=0
        print()
        Q.append(now)


if __name__ == "__main__":
    print("------------미로탈출------------")
    print("-------------------------------")
    print()
    n = int(input("ㅁ*ㅁ 미로를 만들까요?> "))
    maze = make_maze(n)
    for i in range(n):
        print(maze[i])
    find_path(0, 0)


    print(f"{cnt}번만에 탈출에 성공하였습니다.")
    print("탈출 경로> ", end = ' ')
    while Q:
        if len(Q) == 1:
            print(Q.popleft())
            break
        print(Q.popleft(), end = '> ')
    time.sleep(5)
    sys.exit(1)