def add_session():
    # prompt for subject
    while True:
        subject = input("enter subject/course: ").strip()
        if subject:
            subject = subject.title()
            break
        else:
            print("INVALID INPUT")

    # prompt for minutes
    while True:
        time = input("enter minutes studied: ").strip()
        if time.isdigit() and int(time) >= 0 and int(time) <= 1440:  # Assuming a day has 1440 minutes
            minute = int(time)
            break
        else:
            print("INVALID INPUT")

    # prompt for location
    while True:
        location = input("enter location: (Home/Library/Lab/Other)").strip()
        if location:
            location = location.title()
            break
        else:
            print("INVALID INPUT")

    #prompt for notes

    note = input("enter notes (optional): ").strip()
    if note:
        note = note
    else:
        note = "None."
