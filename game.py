import scenarios
from Player import Player

# Create a new player
player_name = input("What is your name? ")
player = Player(player_name)

# Ask the player to choose a scenario
print("Choose a scenario:")
for i, scenario in enumerate(scenarios.scenarios.values()):
    print(f"{i + 1}. {scenario['name']}")
scenario_choice = int(input("Enter the number of the scenario: ")) - 1
scenario = list(scenarios.scenarios.values())[scenario_choice]

# Display the scenario details
print(f"You have chosen the {scenario['name']} scenario.")
print(scenario['description'])

# Ask the player to specify parameters
print("Specify the parameters:")
for key, value in scenario.items():
    if key not in ['name', 'description']:
        new_value = input(f"{key} (default: {value}): ")
        if new_value:
            scenario[key] = type(value)(new_value)

# Process the data
# TODO: implement data processing

# Provide feedback
# TODO: provide feedback on player's performance

# Level up the player
# TODO: increase player's level if scenario completed successfully

# Repeat for additional scenarios
# TODO: repeat for additional scenarios
