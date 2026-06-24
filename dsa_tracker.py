from questions import questions


def view_topics():
    print("\n===== Topics =====")

    for i, topic in enumerate(questions.keys(), start=1):
        total = len(questions[topic])
        completed = sum(q["completed"] for q in questions[topic])

        print(f"{i}. {topic} ({completed}/{total})")


def view_questions():
    topics = list(questions.keys())

    view_topics()

    try:
        choice = int(input("\nSelect Topic Number: "))

        if 1 <= choice <= len(topics):

            topic = topics[choice - 1]

            print(f"\n===== {topic} =====")

            for i, q in enumerate(questions[topic], start=1):

                status = "✓" if q["completed"] else " "

                print(
                    f"{i}. [{status}] {q['name']} "
                    f"({q['difficulty']})"
                )

        else:
            print("Invalid Topic!")

    except ValueError:
        print("Please enter a valid number!")


def mark_complete():
    topics = list(questions.keys())

    view_topics()

    try:
        topic_choice = int(input("\nSelect Topic Number: "))

        if not (1 <= topic_choice <= len(topics)):
            print("Invalid Topic!")
            return

        topic = topics[topic_choice - 1]

        print(f"\n===== {topic} =====")

        for i, q in enumerate(questions[topic], start=1):

            status = "✓" if q["completed"] else " "

            print(
                f"{i}. [{status}] {q['name']} "
                f"({q['difficulty']})"
            )

        question_choice = int(
            input("\nEnter Question Number: ")
        )

        if 1 <= question_choice <= len(questions[topic]):

            questions[topic][question_choice - 1][
                "completed"
            ] = True

            print("Question marked complete!")

        else:
            print("Invalid Question!")

    except ValueError:
        print("Please enter a valid number!")


def show_dashboard():

    total_questions = 0
    completed_questions = 0

    easy = 0
    medium = 0
    hard = 0

    for topic in questions:

        for q in questions[topic]:

            total_questions += 1

            if q["completed"]:

                completed_questions += 1

                if q["difficulty"] == "Easy":
                    easy += 1

                elif q["difficulty"] == "Medium":
                    medium += 1

                elif q["difficulty"] == "Hard":
                    hard += 1

    progress = (
        completed_questions / total_questions
    ) * 100

    print("\n===== USER DASHBOARD =====")

    print(f"Questions Solved : {completed_questions}")
    print(f"Easy Solved      : {easy}")
    print(f"Medium Solved    : {medium}")
    print(f"Hard Solved      : {hard}")

    print(
        f"\nOverall Progress : {progress:.1f}%"
    )


while True:

    print("\n==========================")
    print("      PREPGENIUS AI")
    print("==========================")

    print("1. View Topics")
    print("2. View Questions")
    print("3. Mark Question Complete")
    print("4. Show Dashboard")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        view_topics()

    elif choice == "2":
        view_questions()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        show_dashboard()

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("Invalid Choice!")