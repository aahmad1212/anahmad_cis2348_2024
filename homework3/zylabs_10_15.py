# Adil Ahmad
# 2278219
class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        percentage = self.wins / (self.wins + self.losses)
        return percentage

    def print_standing(self):
        if self.wins > self.losses:
            print(f"Congratulations, Team {self.name} has a winning average!")
        elif self.wins < self.losses:
            print(f"Team {self.name} has a losing average.")


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()
