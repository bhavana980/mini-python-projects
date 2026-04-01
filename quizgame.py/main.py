import random
from questions import questions

def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def play_quiz():
    print("\n🐍 Python Quiz Game 🐍")

    choice = input("Select Difficulty (easy/medium/hard): ").lower()

    if choice not in questions:
        print("Invalid choice!")
        return

    quiz_questions = questions[choice]
    random.shuffle(quiz_questions)

    score = 0

    for q in quiz_questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        answer = input("Enter your answer: ").lower()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

    print("\n----------------------")
    print(f"Your Score: {score}/{len(quiz_questions)} ⭐")

    high_score = load_high_score()

    if score > high_score:
        print("🎉 New High Score!")
        save_high_score(score)
    else:
        print(f"🏆 High Score: {high_score}")

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Play Quiz")
        print("2. View High Score")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_quiz()
        elif choice == "2":
            print(f"🏆 High Score: {load_high_score()}")
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()