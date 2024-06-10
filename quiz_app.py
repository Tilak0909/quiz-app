import tkinter as tk
from tkinter import messagebox

# Defining the questions, options, and answers
questions = [
    {
        "question": "How many players are there in a cricket team?",
        "options": ["9", "11", "15", "12"],
        "answer": "11"
    },
    {
        "question": "How many balls are there in an over?",
        "options": ["8", "5", "6", "10"],
        "answer": "6"
    },
    {
        "question": "What is the name of the international T20 cricket league held in India?",
        "options": ["Indian Premier League", "International Premier league", "Indian Players League", "International Players legecy"],
        "answer": "Indian Premier League"
    },
    {
        "question": "Which Indian Cricketer is popularly known as Thala?",
        "options": ["Virat Kolhi", "Rohit Sharma", "Kapil Dev", "Mahendra Singh Dhoni"],
        "answer": "Mahendra Singh Dhoni"
    }
]

# Initialize the current question index
current_question_index = 0

def check_answer(selected_option):
    global current_question_index
    correct_answer = questions[current_question_index]["answer"]
    
    if selected_option == correct_answer:
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect! The correct answer is {correct_answer}.", fg="red")
    
    next_question()

def next_question():
    global current_question_index
    current_question_index += 1
    
    if current_question_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
        root.destroy()

def load_question():
    question_label.config(text=questions[current_question_index]["question"])
    options = questions[current_question_index]["options"]
    for i, option in enumerate(options):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

# Initialize the main window
root = tk.Tk()
root.title("Quiz Game")

# Create and place the question label
question_label = tk.Label(root, text="", font=('Helvetica', 16))
question_label.pack(pady=20)

# Create and place the option buttons
option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=('Helvetica', 16))
    button.pack(pady=5, fill=tk.X)
    option_buttons.append(button)

# Create and place the feedback label
feedback_label = tk.Label(root, text="", font=('Helvetica', 16))
feedback_label.pack(pady=10)

# Load the first question
load_question()

# Run the main event loop
root.mainloop()
