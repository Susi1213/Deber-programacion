import tkinter as tk
from tkinter import messagebox, ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x450")

        self.initialize_ui()

        # Atajos de teclado
        self.setup_keyboard_shortcuts()

    def initialize_ui(self):
        # Frame para la entrada y botón de añadir tarea
        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)

        self.new_task_entry = tk.Entry(add_frame, width=40)
        self.new_task_entry.grid(row=0, column=0)

        self.add_task_button = tk.Button(add_frame, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10)

        # Frame para los botones de manejo de tareas
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.mark_task_button = tk.Button(button_frame, text="Marcar como Completada", command=self.mark_task)
        self.mark_task_button.grid(row=0, column=0, padx=10)

        self.unmark_task_button = tk.Button(button_frame, text="Desmarcar Tarea", command=self.unmark_task)
        self.unmark_task_button.grid(row=0, column=1, padx=10)

        self.delete_task_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=2, padx=10)

        # Lista de tareas
        self.tasks_frame = ttk.Frame(self.root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.tasks_list = ttk.Treeview(self.tasks_frame, columns=("Tarea"), show="headings")
        self.tasks_list.heading("Tarea", text="Descripción")
        self.tasks_list.pack(fill=tk.BOTH, expand=True)

    def setup_keyboard_shortcuts(self):
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('c', lambda e: self.mark_task())  # Tecla 'C' para marcar como completada
        self.root.bind('u', lambda e: self.unmark_task())  # Tecla 'U' para desmarcar tarea
        self.root.bind('d', lambda e: self.delete_task())  # Tecla 'D' para eliminar
        self.root.bind('<Delete>', self.delete_task)  # Tecla 'Delete' para eliminar
        self.root.bind('<Return>', lambda e: self.mark_task() if self.tasks_list.selection() else self.add_task())

    def add_task(self, event=None):
        task = self.new_task_entry.get().strip()
        if task:
            if not self.task_exists(task):
                self.tasks_list.insert('', tk.END, values=(task,))
                self.new_task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "La tarea ya existe.")
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def mark_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('completed',))
            self.tasks_list.tag_configure('completed', background='light green')

    def unmark_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('uncompleted',))
            self.tasks_list.tag_configure('uncompleted', background='white')

    def delete_task(self, event=None):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.delete(selected_item)
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para eliminar.")

    def task_exists(self, task):
        tasks = self.tasks_list.get_children()
        for item in tasks:
            if self.tasks_list.item(item, 'values')[0] == task:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
