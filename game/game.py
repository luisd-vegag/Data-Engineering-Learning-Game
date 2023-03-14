import time
from scenarios.scenarios import scenarios
from scenarios.scenario_001 import data_processing
from game.player import Player
import generate_data as gd
import compute_measurements as cm


def main():
    # Create a new player
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Display list of scenarios
    print("Available Scenarios:")
    for i, scenario in enumerate(scenarios):
        print(f"{i}: {scenario['name']}")

    # Prompt user to select a scenario
    scenario_index = int(
        input("Please select a scenario by entering its index number: "))
    if scenario_index >= len(scenarios):
        print("Invalid scenario index. Please select a number between 0 and {}".format(
            len(scenarios) - 1))
        return
    scenario = scenarios[scenario_index]
    print(f"Description: {scenario['description']}")

    # Display list of scenarios
    print("Available Methods:")
    for i, method in enumerate(scenario["methods"]):
        print(f"{i}: {method}")
    # Prompt user to select processing method
    method_index = int(
        input("Please select a method to run this scenario by entering its index number: "))

    if method_index >= len(scenario['methods']):
        print(
            f"Invalid method index. Please select a number between 0 and {len(scenario['methods']) - 1}")
        return
    selected_method = scenario['methods'][method_index]
    # Prompt user to ask if want to compare avaiabe methods
    compare_methods = input(
        "Do you want to compare the available methods? (y/n): ")
    if compare_methods.lower() == "y":
        compare_methods = True
    elif compare_methods.lower() == "n":
        compare_methods = False
    else:
        print("Invalid response.")
        return

    # Generate csv files
    input_files = gd.generate_csv_files(
        path='system/data_10k/', num_rows=10000)

    processing_results = list()

    if compare_methods:
        for method in scenario['methods']:
            print(f'Processing {method}')
            results, cpu_time, cpu_total_usage, cpu_usage = data_processing.run_scenario(
                scenario, input_files, method)
            processing_results.append(
                {'method': method, 'cpu_time': cpu_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage})
    else:
        print(f'Processing {selected_method}')
        results, cpu_time, cpu_total_usage, cpu_usage = data_processing.run_scenario(
            scenario, input_files, selected_method)
        processing_results.append(
            {'method': selected_method, 'cpu_time': cpu_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage})

    # gd.delete_files(input_files)

    methods_comparation = cm.compare_method(
        selected_method, processing_results)


if __name__ == '__main__':
    main()
