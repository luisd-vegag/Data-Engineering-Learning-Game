from scenarios import scenarios
from game.player import Player

'''
    #FIXME: 
        - Scenario 3, there is a print that show the creation file progess. It should be removed.
        - Scenario 4. when removing a column there is a bug that fail the execution. Syntax error.
'''


def group_scenarios_by_topic(scenarios):
    topics = {}
    for scenario in scenarios:
        if 'topic' not in scenario:
            topic = 'Miscellaneous'
        else:
            topic = scenario['topic']
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(scenario)
    return topics


def display_topics(topics):
    print("\nAvailable Topics:")
    for i, topic in enumerate(sorted(topics.keys())):
        print(f"{i+1}: {topic}")


def display_scenarios(scenarios):
    print("\nAvailable Scenarios:")
    for i, scenario in enumerate(scenarios):
        print(f"{i+1}: {scenario['name']}\n{scenario['description']}\n")


def main():
    # Display welcome message
    print("Welcome to the Data Engineering Learning Game!")
    print("Choose a scenario to begin learning about data engineering.")

    while True:
        # Group scenarios by topic
        topics = group_scenarios_by_topic(scenarios)

        # Prompt user to select a topic or quit
        while True:
            display_topics(topics)
            user_input = input(
                "\nEnter the number of the topic you want to explore, or 'q' to quit: ")
            if user_input.lower() == 'q':
                print('Goodbye and good luck in your Data Engineering learning journey!')
                return
            try:
                topic_index = int(user_input) - 1
                if topic_index < 0 or topic_index >= len(topics):
                    raise ValueError
                break
            except ValueError:
                print(
                    "Invalid input. Please enter a number between 1 and", len(topics))

        # Display scenarios for selected topic and prompt user to select a scenario or go back to topic selection
        topic = sorted(topics.keys())[topic_index]
        scenarios_for_topic = topics[topic]
        while True:
            display_scenarios(scenarios_for_topic)
            user_input = input(
                "\nEnter the number of the scenario you want to play, or 'b' to go back to topic selection: ")
            if user_input.lower() == 'b':
                break
            try:
                scenario_index = int(user_input)-1
                if scenario_index < 0 or scenario_index >= len(scenarios_for_topic):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and",
                      len(scenarios_for_topic))

        # Run the selected scenario
        if user_input.lower() != 'b':
            while True:
                scenario = scenarios_for_topic[scenario_index]
                scenario_module = scenario['module']
                scenario_description = scenario['description']
                print(
                    f"\nYou have chosen scenario '{scenario['name']}': {scenario_description}\n")
                scenario_module.run_scenario(scenario)
                user_input = input(
                    "\nDo you want to retry the scenario? (y/n) ")
                if user_input.lower() == 'n':
                    break

        # Ask the user if they want to explore another topic
        while True:
            user_input = input(
                "\nDo you want to explore another topic? (y/n) ")
            if user_input.lower() == 'y':
                break
            elif user_input.lower() == 'n':
                print('Goodbye and good luck in your Data Engineering learning journey!')
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
