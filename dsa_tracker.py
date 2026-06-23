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

    choice = int(input("\nSelect Topic Number: "))

    if 1 <= choice <= len(topics):
        topic = topics[choice - 1]

        print(f"\n===== {topic} =====")

        for i, q in enumerate(questions[topic], start=1):
            status = "✓" if q["completed"] else " "

            print(f"{i}. [{status}] {q['name']}")


def mark_complete():
    topics = list(questions.keys())

    view_topics()

    topic_choice = int(input("\nSelect Topic Number: "))

    if not (1 <= topic_choice <= len(topics)):
        print("Invalid Topic!")
        return

    topic = topics[topic_choice - 1]

    print(f"\n===== {topic} =====")

    for i, q in enumerate(questions[topic], start=1):
        status = "✓" if q["completed"] else " "

        print(f"{i}. [{status}] {q['name']}")

    question_choice = int(input("\nEnter Question Number: "))

    if 1 <= question_choice <= len(questions[topic]):
        questions[topic][question_choice - 1]["completed"] = True

        print("Question marked complete!")
    else:
        print("Invalid Question!")


def show_progress():
    total_questions = 0
    completed_questions = 0

    print("\n===== Progress =====")

    for topic in questions:
        total = len(questions[topic])
        completed = sum(q["completed"] for q in questions[topic])

        total_questions += total
        completed_questions += completed

        percentage = (completed / total) * 100

        print(
            f"{topic}: {completed}/{total} ({percentage:.1f}%)"
        )

    overall = (
        completed_questions / total_questions
    ) * 100

    print("\n----------------------")
    print(
        f"Overall: {completed_questions}/{total_questions}"
    )
    print(f"Progress: {overall:.1f}%")


while True:

    print("\n===== PrepGenius AI =====")
    print("1. View Topics")
    print("2. View Questions")
    print("3. Mark Question Complete")
    print("4. Show Progress")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        view_topics()

    elif choice == "2":
        view_questions()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        show_progress()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")