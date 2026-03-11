from tracker import add_session, view_all, view_summary

def main():
    print("Welcome to Study Session Tracker!")

    while True:
        print("1. Add Study Session")
        print("2. View Summary")
        print("3. View All Sessions")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_session()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_all()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–4.\n")

if __name__ == "__main__":
    main()
