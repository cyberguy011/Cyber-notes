topics = []

while True:
    topic = input("Enter topic (or quit): ")

    if topic.lower() == "quit":
        break

    topics.append(topic)

print("\nYour Topics:")
for item in topics:
    print("-", item)
