import random

if __name__ == "__main__":
    class Players:
        tried = 0
        made = 0
        score = 0

        def __init__(self, name, number, shoot):
            self.name = name
            self.number = number
            self.shoot = shoot

        def threepoint(self):
            result = random.choices(range(0,2), weights = [5, 1+self.shoot])
            if result[0] == 0:
                Players.tried+=1
                print(f"Missed! {Players.made} of {Players.tried}")
            else:
                Players.tried+=1
                Players.made+=1
                Players.score+=3
                print(f"Made! {Players.made} of {Players.tried}")

        def midrange(self):
            result = random.choices(range(0, 2), weights=[4, 1 + self.shoot])
            if result[0] == 0:
                Players.tried += 1
                print(f"Missed! {Players.made} of {Players.tried}")
            else:
                Players.tried += 1
                Players.made += 1
                Players.score += 2
                print(f"Made! {Players.made} of {Players.tried}")

        def freethrow(self):
            result = random.choices(range(0, 2), weights=[3, 1 + self.shoot])
            if result[0] == 0:
                Players.tried += 1
                print(f"Missed! {Players.made} of {Players.tried}")
            else:
                Players.tried += 1
                Players.made += 1
                Players.score += 1
                print(f"Made! {Players.made} of {Players.tried}")

        def totalscore(self):
            print(f"Total Score: {Players.score}")

    player1 = Players("Curry", 23, 3)
    player1.threepoint()
    player1.threepoint()
    player1.threepoint()
    player1.threepoint()
    player1.midrange()
    player1.freethrow()
    player1.totalscore()