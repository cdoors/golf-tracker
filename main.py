import json
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize an empty list to store golf round data
golf_data = []
goals = []

# Function to add a new golf round entry
def add_round():
    round_entry = {}
    round_entry['course'] = simpledialog.askstring("Input", "Enter course name:")
    round_entry['date'] = simpledialog.askstring("Input", "Enter date (MM/DD/YYYY):")
    round_entry['score'] = simpledialog.askinteger("Input", "Enter score:")
    round_entry['putts'] = simpledialog.askinteger("Input", "Enter number of putts:")
    round_entry['fairways_hit'] = simpledialog.askinteger("Input", "Enter number of fairways hit:")
    round_entry['greens_in_regulation'] = simpledialog.askinteger("Input", "Enter number of greens in regulation:")
    round_entry['notes'] = simpledialog.askstring("Input", "Enter any additional notes:")

    golf_data.append(round_entry)

    # Save golf data to a JSON file
    with open('golf_data.json', 'w') as f:
        json.dump(golf_data, f)

    messagebox.showinfo("Info", "Round entry added successfully!")

# Function to show scoring trends over time
def show_scoring_trends():
    scores = [entry['score'] for entry in golf_data]
    dates = [entry['date'] for entry in golf_data]
    plt.plot(dates, scores, marker='o')
    plt.title('Scoring Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.show()

# Function to set and track golfing goals
def set_goals():
    goal = simpledialog.askstring("Input", "Enter your goal:")
    goals.append(goal)
    messagebox.showinfo("Info", "Goal set successfully!")

# Function to show golf statistics
def show_statistics():
    if not golf_data:
        messagebox.showinfo("Info", "No data available.")
        return

    total_rounds = len(golf_data)
    average_score = sum(entry['score'] for entry in golf_data) / total_rounds
    average_putts = sum(entry['putts'] for entry in golf_data) / total_rounds
    stats = f"Total Rounds: {total_rounds}\nAverage Score: {average_score:.2f}\nAverage Putts: {average_putts:.2f}"
    messagebox.showinfo("Golf Statistics", stats)

# Load existing golf data from JSON file (if available)
try:
    with open('golf_data.json', 'r') as f:
        golf_data = json.load(f)
except FileNotFoundError:
    pass

# Create the main application window using Tkinter
def main():
    root = tk.Tk()
    root.title("Golf Score Tracker")

    tk.Button(root, text="Add Round", command=add_round).pack()
    tk.Button(root, text="Show Scoring Trends", command=show_scoring_trends).pack()
    tk.Button(root, text="Set Goals", command=set_goals).pack()
    tk.Button(root, text="Show Statistics", command=show_statistics).pack()
    tk.Button(root, text="Exit", command=root.quit).pack()

    root.mainloop()

if __name__ == "__main__":
    main()

