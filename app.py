while True:
    print("\n=== Cyber Notes ===")
    print("1. View Topics")
    print("2. Add Topic")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            with open("topics.txt", "r") as file:
                topics = file.readlines()

            print("\nSaved Topics:")
            for number, topic in enumerate(topics, start=1):
                print(f"{number}. {topic.strip()}")

        except FileNotFoundError:
            print("No topics file found.")

    elif choice == "2":
        topic = input("Enter new topic: ")

        with open("topics.txt", "a") as file:
            file.write(topic + "\n")

        print("Topic saved!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
