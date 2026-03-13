from data import subjects, minutes, locations, notes

def add_session():
    # prompt for subject
    while True:
        subject = input("Enter subject/course: ").strip()
        if subject:
            subject = subject.title()
            break
        else:
            print("INVALID INPUT")

    # prompt for minutes
    while True:
        time = input("Enter minutes studied: ").strip()
        if time.isdigit() and int(time) >= 0 and int(time) <= 1440:
            minute = int(time)
            break
        else:
            print("INVALID TIME")

    # prompt for location
    valid_locations = {"Home", "Library", "Lab", "Other"}
    while True:
        location = input("Enter location (Home/Library/Lab/Other): ").strip()
        if location.title() in valid_locations:
            location = location.title()
            break
        else:
            print("INVALID LOCATION")

    # prompt for notes
    note = input("Enter notes (optional): ").strip()
    if note:
        note = note
    else:
        note = "None."

    # store session data
    subjects.append(subject)
    minutes.append(minute)
    locations.append(location)
    notes.append(note)

    print(f"Studied {subject} for {minute} minutes at {location}\nSession added.")


def view_all():
    if len(subjects) == 0:
        print("No study sessions recorded.\n")
        return

    print("\nAll Study Sessions:")
    for i in range(len(subjects)):
        print(f"\nSession {i + 1}")
        print(f"Subject  : {subjects[i]}")
        print(f"Minutes  : {minutes[i]}")
        print(f"Location : {locations[i]}")
        print(f"Notes    : {notes[i]}")
    print()


def view_summary():
    if len(minutes) == 0:
        print("No study sessions recorded.\n")
        return

    total_sessions = len(minutes)
    total_minutes = sum(minutes)
    average_minutes = total_minutes / total_sessions
    longest_session = max(minutes)
    shortest_session = min(minutes)

    print("\nStudy Session Summary")
    print(f"Total sessions        : {total_sessions}")
    print(f"Total minutes studied : {total_minutes}")
    print(f"Average minutes       : {average_minutes:.2f}")
    print(f"Longest session       : {longest_session}")
    print(f"Shortest session      : {shortest_session}\n")