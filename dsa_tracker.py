questions = []

while True:
    print("\n===== PrepGenius AI =====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Question Name: ")
        topic = input("Enter Topic: ")
        difficulty = input("Enter Difficulty: ")

        question = {
            "name": name,
            "topic": topic,
            "difficulty": difficulty
        }

        questions.append(question)

        print("Question Added!")

    elif choice == "2":
        print("\nSolved Questions:")

        for i, q in enumerate(questions, start=1):
            print(f"\n{i}. {q['name']}")
            print(f"   Topic: {q['topic']}")
            print(f"   Difficulty: {q['difficulty']}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")