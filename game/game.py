from scenarios import scenarios
from game.player import Player


def main():
    # Create a new player
    # player_name = input("Enter your name: ")
    # player = Player(player_name)

    # Display list of scenarios
    print("Available Scenarios:")
    for i, scenario in enumerate(scenarios):
        print(f"{i}: {scenario['name']}")

    # Prompt user to select a scenario
    scenario_index = int(
        input("Please select a scenario by entering its index number: "))

    scenario_id = str(f"{scenario_index+1:03}")
    scenario_ids = [str(scenario['id']) for scenario in scenarios]
    if scenario_id not in scenario_ids:
        print(
            f"Invalid scenario index. Please select a number between 0 and {len(scenarios)-1}")
        return

    scenario_module = scenarios[scenario_index]['module']
    scenario_description = scenarios[scenario_index]['description']
    print(f"Description: {scenario_description}")

    scenario_module.run_scenario(
        scenarios[scenario_index])


if __name__ == '__main__':
    main()
