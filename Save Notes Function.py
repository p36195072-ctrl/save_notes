def save_notes(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

save_notes("Hello")
