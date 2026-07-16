# ==========================
# Deek v1.0
# Main Application
# ==========================

from brain import DeekBrain


def main():

    print("=" * 35)
    print("🤖 Deek v1.0")
    print("=" * 35)

    print("\nHi Boss! 👋")
    print("Type 'exit' to quit.\n")

    brain = DeekBrain()

    while True:

        question = input("You: ").strip()

        if question.lower() in [

            "exit",
            "quit",
            "bye"

        ]:

            print("\nDeek: Goodbye Boss! 👋")
            break

        answer = brain.ask(question)

        print("\nDeek:")
        print(answer)
        print()


if __name__ == "__main__":
    main()
