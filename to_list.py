import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def del_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task = task_list.get(selected_task_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_task)

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        window.destroy()

# Create the main application window
window = tk.Tk()
window.title("To-Do List")

window_width = 500
window_height = 270
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Entry box to add tasks
entry = tk.Entry(window, width=60)
entry.pack(pady=10, padx=10)

# Listbox to display the tasks
task_list = tk.Listbox(window, width=50, height=10, bg="pink")
task_list.pack(pady=10, padx=10)

# Buttons for managing tasks
button_frame = tk.Frame(window)
button_frame.pack()

add = tk.Button(button_frame, text="Add",bg="pink", command=add_task)
add.pack(side=tk.LEFT, padx=10)

delete = tk.Button(button_frame, text="Delete", bg="pink", command=del_task)
delete.pack(side=tk.LEFT, padx=10)

edit = tk.Button(button_frame, text="Edit",bg="pink", command=edit_task)
edit.pack(side=tk.LEFT, padx=10)

exit = tk.Button(button_frame, text="Exit",bg="pink", command=exit_app)
exit.pack(side=tk.LEFT, padx=10)

# Start the main event loop
window.mainloop()
