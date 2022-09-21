import heapq

# implementation of dijkstra algorithm
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


if __name__ == "__main__":
    INF = 2147000000

    # v: number of Vertices, e: number of Edges
    v, e = map(int, input().split())

    # starting node
    start = int(input())

    # 2-dimension-list containing connection status of vertices
    graph = [[] for i in range(v+1)]

    # initializing minimum-distance
    distance = [INF] * (v + 1)

    # checking information of every edge
    for _ in range(e):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        