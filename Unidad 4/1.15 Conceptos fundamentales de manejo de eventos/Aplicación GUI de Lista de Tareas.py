import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        self.label_task = tk.Label(root, text="Tarea:")
        self.label_task.pack()

        self.entry_task = tk.Entry(root, width=40)
        self.entry_task.pack(pady=5)

        self.label_description = tk.Label(root, text="Descripción:")
        self.label_description.pack()

        self.entry_description = tk.Entry(root, width=40)
        self.entry_description.pack(pady=5)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.undo_button = tk.Button(root, text="Desmarcar Tarea", command=self.undo_task)
        self.undo_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=60, height=15, selectmode=tk.MULTIPLE)
        self.task_list.pack(padx=10, pady=10)

        self.entry_task.bind("<Return>", self.add_task_enter)

    def add_task(self):
        task = self.entry_task.get()
        description = self.entry_description.get()
        if task:
            self.tasks.append({"task": task, "description": description, "completed": False})
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def add_task_enter(self, event):
        self.add_task()

    def complete_task(self):
        selected_indices = self.task_list.curselection()
        if selected_indices:
            for index in selected_indices:
                self.tasks[index]["completed"] = True
                self.task_list.itemconfig(index, {'bg': 'light green'})
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def undo_task(self):
        selected_indices = self.task_list.curselection()
        if selected_indices:
            for index in selected_indices:
                self.tasks[index]["completed"] = False
                self.task_list.itemconfig(index, {'bg': 'white'})
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para desmarcar.")

    def delete_task(self):
        selected_indices = self.task_list.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            task_text = "[X] " + task["task"] if task["completed"] else "[ ] " + task["task"]
            task_text += " - " + task["description"]
            self.task_list.insert(tk.END, task_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
