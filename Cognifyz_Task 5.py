# Cognifyz Technology Software Development Intern 
# Level 3 :-
# Task 5
#Enhance the CRUD application to store task data persistently using file I/O
#Objective: Implement file storage for tasksto enable saving and loading from a text file

from tkinter import *

class Task:
    DATA_FILE = "tasks.txt"

    def __init__(self):
        self.list_tasks = []
        self.screen = Tk()
        self.screen.config(padx=100, pady=100)

        self.load_tasks()  # Load tasks from file on startup

        # UI elements
        self.entry_input = Entry(width=36)
        self.entry_input.grid(row=1, column=1, columnspan=2, pady=10)
        self.entry_input.focus()

        self.label_info = Label(text="Enter Your Task in 'Your Format Should be Task Number : Task Details'")
        self.label_info.grid(row=0, column=1, columnspan=2)

        self.button_create_task = Button(text="Create A New Task", pady=10, border=1, command=self.create_task)
        self.button_create_task.grid(row=2, column=1, columnspan=2, pady=10)

        self.button_read_task = Button(text="Display Tasks", pady=10, border=1, command=self.read_tasks)
        self.button_read_task.grid(row=3, column=1, columnspan=2, pady=10)

        self.button_update_task = Button(text="Update", pady=10, border=1, command=self.update_tasks)
        self.button_update_task.grid(row=4, column=1, columnspan=2, pady=10)

        self.button_delete_task = Button(text="Delete Task", pady=10, border=1, command=self.delete_task)
        self.button_delete_task.grid(row=5, column=1, columnspan=2, pady=10)

        self.label_outputinfo = Label(text="")
        self.label_outputinfo.grid(row=6, column=1, columnspan=2, pady=10)

        self.task_listbox = Listbox(width=50, height=10)
        self.task_listbox.grid(row=7, column=1, columnspan=2, pady=10)

        self.read_tasks()  # Display loaded tasks on startup

        self.screen.mainloop()

    def save_tasks(self):
        try:
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                for task in self.list_tasks:
                    f.write(task + "\n")
        except Exception as e:
            self.label_outputinfo.config(text=f"Error saving tasks: {e}")

    def load_tasks(self):
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                self.list_tasks = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            # No file yet, start with empty list
            self.list_tasks = []
        except Exception as e:
            self.list_tasks = []
            print(f"Error loading tasks: {e}")

    def create_task(self):
        task_text = self.entry_input.get()
        if task_text:
            self.list_tasks.append(task_text)
            self.entry_input.delete(0, END)
            self.label_outputinfo.config(text="Task added.")
            self.save_tasks()
            self.read_tasks()
        else:
            self.label_outputinfo.config(text="No Entry Was Provided")

    def read_tasks(self):
        self.task_listbox.delete(0, END)
        if len(self.list_tasks) == 0:
            self.label_outputinfo.config(text="No Tasks Added")
        else:
            for task in self.list_tasks:
                self.task_listbox.insert(END, task)
            self.label_outputinfo.config(text=f"{len(self.list_tasks)} task(s) loaded.")

    def update_tasks(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
        except IndexError:
            self.label_outputinfo.config(text="Please select a task to update.")
            return

        new_task_text = self.entry_input.get()
        if not new_task_text:
            self.label_outputinfo.config(text="Please enter new task text in the entry field.")
            return

        self.list_tasks[selected_index] = new_task_text
        self.save_tasks()
        self.read_tasks()
        self.entry_input.delete(0, END)
        self.label_outputinfo.config(text="Task updated successfully.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
        except IndexError:
            self.label_outputinfo.config(text="Please select a task to delete.")
            return

        removed_task = self.list_tasks.pop(selected_index)
        self.save_tasks()
        self.read_tasks()
        self.label_outputinfo.config(text=f"Task deleted: {removed_task}")

if __name__ == "__main__":
    Task()
