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
        if time.isdigit() and int(time) >= 0 and int(time) <= 1440:  # Assuming a day has 1440 minutes
            minute = int(time)
            break
        else:
            print("INVALID TIME")

    # prompt for location
    valid_locations = {"Home", "Library", "Lab", "Other"}
    while True:
        location = input("Enter location: (Home/Library/Lab/Other)").strip()
        if location.title() in valid_locations:
            location = location.title()
            break
        else:
            print("INVALID LOCATION")

    #prompt for notes

    note = input("Enter notes (optional): ").strip()
    if note:
        note = note
    else:
        note = "None."

    #store session data
    subjects.append(subject)
    minutes.append(minute)
    locations.append(location)
    notes.append(note)

    print(f"Studied {subject} for {minute} minutes at {location}\nSession added.")