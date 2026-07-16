# ==========================
# Deek v1.1
# Main Application
# ==========================

from controller import DeekController


def main():

    print("=" * 35)
    print("🤖 Deek v1.1")
    print("=" * 35)

    print("\nHi Boss! 👋")
    print("Type 'exit' to quit.\n")

    deek = DeekController()

    while True:

        question = input("You: ").strip()

        if question.lower() in [
            "exit",
            "quit",
            "bye"
        ]:

            print("\nDeek: Goodbye Boss! 👋")
            break

        answer = deek.process(question)

        print("\nDeek:")
        print(answer)
        print()


if __name__ == "__main__":
    main()
