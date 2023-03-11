import time
from scenarios.scenarios import scenarios
from data_processing import data_processing
from player import Player
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

    # Generate csv files
    # input_files = gd.generate_csv_files(
    #    path='system/data_10k/', num_rows=10000)

    # input_files = ['system/data_10k/users.csv', 'system/data_10k/sales.csv',
    #               'system/data_10k/products.csv', 'system/data_10k/customers.csv']
    input_files = ['system/data_100k/users.csv', 'system/data_100k/sales.csv',
                   'system/data_100k/products.csv', 'system/data_100k/customers.csv']
    # input_files = ['system/data_1m/users.csv', 'system/data_1m/sales.csv',
    #                'system/data_1m/products.csv', 'system/data_1m/customers.csv']

    processing_results = list()

    for method in scenario['methods']:
        time.sleep(2)
        print(f'Processing {method}')
        results, cpu_time, cpu_total_usage, cpu_usage = data_processing.run_scenario(
            scenario, input_files, method)
        processing_results.append(
            {'method': method, 'cpu_time': cpu_time, 'cpu_total_usage': cpu_total_usage, 'cpu_usage': cpu_usage})

    # gd.delete_files(input_files)

    methods_comparation = cm.compare_method(
        selected_method, processing_results)


if __name__ == '__main__':
    main()
