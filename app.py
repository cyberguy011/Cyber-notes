print("=== Cyber Notes ===\n")

with open("topics.txt", "r") as file:
    topics = file.readlines()

for number, topic in enumerate(topics, start=1):
    print(f"{number}. {topic.strip()}")
