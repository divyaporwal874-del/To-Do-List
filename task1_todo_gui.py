
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first!")
    else:
        index = selected[0]
        task_list.delete(index)
        tasks.pop(index)

def complete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first!")
    else:
        index = selected[0]
        task = tasks[index]

        task_list.delete(index)
        task_list.insert(index, "✔ " + task)

        tasks[index] = "✔ " + task

# Main Window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x550")
root.config(bg="#E8EAF6")

# Heading
heading = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold"),
    bg="#E8EAF6",
    fg="#303F9F"
)
heading.pack(pady=25)

# Input Box
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    bd=2
)
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(
    root,
    text="ADD TASK",
    font=("Arial", 12, "bold"),
    bg="#3949AB",
    fg="white",
    width=20,
    command=add_task
)
add_button.pack(pady=8)

# Task List
task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=38,
    height=12,
    selectbackground="#7986CB"
)
task_list.pack(pady=15)

# Complete Button
complete_button = tk.Button(
    root,
    text="MARK COMPLETED",
    font=("Arial", 11, "bold"),
    bg="#43A047",
    fg="white",
    width=20,
    command=complete_task
)
complete_button.pack(pady=5)

# Delete Button
delete_button = tk.Button(
    root,
    text="DELETE TASK",
    font=("Arial", 11, "bold"),
    bg="#E53935",
    fg="white",
    width=20,
    command=delete_task
)
delete_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(
    root,
    text="EXIT",
    font=("Arial", 11, "bold"),
    bg="#424242",
    fg="white",
    width=20,
    command=root.destroy
)
exit_button.pack(pady=10)

root.mainloop()

