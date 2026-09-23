

rooms = {
    "A": "Dirty",
    "B": "Clean"
}

current_room = "A"

while True:
    print(f"\nCurrent room: {current_room}")
    print(f"Room A: {rooms['A']}, Room B: {rooms['B']}")

    if rooms[current_room] == "Dirty":
        print("Action: Cleaning...")
        rooms[current_room] = "Clean"
    else:
        print("Action: Room is already clean.")

    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

    
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean!")
        break