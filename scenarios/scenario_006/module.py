def run_scenario(scenario):
    correct_answers = 0

    print(scenario["description"])
    print("Please answer the following questions:\n")

    for question in scenario["questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option number): ")
        if user_answer == str(question["options"].index(question["correct_option"]) + 1):
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect!")

        print()

    print(f"You answered {correct_answers} out of {len(scenario['questions'])} questions correctly.")

    if correct_answers == len(scenario["questions"]):
        print("Congratulations, you have completed the scenario successfully!")
    else:
        print("Keep practicing to improve your knowledge of OOP concepts.")

