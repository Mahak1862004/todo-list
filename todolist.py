import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Frame for heading
        self.heading_frame = tk.Frame(self.master)
        self.heading_frame.pack()

        # Label for heading
        self.heading_label = tk.Label(self.heading_frame, text="To-Do List", font=("Arial", 18, "bold"), fg="green")
        self.heading_label.pack(pady=10)

        # Frame for input and buttons
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Frame for displaying tasks
        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=50)
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Frame for update and delete buttons
        self.update_delete_frame = tk.Frame(self.master)
        self.update_delete_frame.pack(pady=10)

        self.update_button = tk.Button(self.update_delete_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.update_delete_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Initially hide the update button
        self.update_button.pack_forget()

        # Bind event to show/hide the update button when a task is selected/deselected
        self.task_listbox.bind('<<ListboxSelect>>', self.toggle_update_button)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.update_button.pack_forget()  # Hide the update button after adding task

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
            self.update_button.pack_forget()  # Hide the update button after deleting task

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def toggle_update_button(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.update_button.pack(side=tk.LEFT, padx=5)  
        else:
            self.update_button.pack_forget()  

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
