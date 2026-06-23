questions = []

while True:
    print("\n===== PrepGenius AI =====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        question = input("Enter question name: ")
        questions.append(question)
        print("Question Added!")

    elif choice == "2":
        print("\nSolved Questions:")
        for i, q in enumerate(questions, start=1):
            print(f"{i}. {q}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")