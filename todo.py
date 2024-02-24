import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, width=10)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_listbox = tk.Listbox(self.master, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.complete_button = tk.Button(self.master, text="Mark as Completed", command=self.mark_completed, width=15)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task, width=15)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def mark_completed(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            self.task_listbox.itemconfig(index, {'bg': 'light green'})
            self.tasks[index] = f"[Completed] {self.tasks[index]}"
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
