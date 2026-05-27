Save Notes Function

A beginner-friendly Python project that demonstrates how to save notes into a text file using functions and the with open() statement.

📌 Description

This program:

Creates a function named save_notes()
Opens a file called notes.txt
Saves text into the file
Automatically closes the file using with open()

This method is cleaner and safer than manually using close().

🧠 Concepts Used

Functions
Function Parameters
File Handling
with open()
Append Mode ('a')
write() method
Strings

💻 Code

def save_notes(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

save_notes("Hello")

▶️ Example Output

Hello
