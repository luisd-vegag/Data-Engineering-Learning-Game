class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.skills = []

    def add_experience(self, points):
        self.experience += points
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")

    def add_skill(self, skill):
        self.skills.append(skill)

    def __str__(self):
        return f"{self.name} (Level {self.level})"
