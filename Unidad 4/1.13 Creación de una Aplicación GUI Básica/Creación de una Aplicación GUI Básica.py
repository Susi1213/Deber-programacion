import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class AplicacionGUI:

    def __init__(self, root):
        self.root = root
        root.title("Aplicación GUI Básica")
        root.geometry("300x250")  # Se ha aumentado la altura para dar espacio a los nuevos botones
        self.crear_menu()
        self.crear_interfaz()

    def crear_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Nuevo", command=self.nuevo)
        self.archivo_menu.add_command(label="Abrir", command=self.abrir)
        self.archivo_menu.add_command(label="Guardar", command=self.guardar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.salir)

    def crear_interfaz(self):
        self.etiqueta = tk.Label(self.root, text="Ingrese información:")
        self.etiqueta.pack()
        self.entrada_texto = tk.Entry(self.root)
        self.entrada_texto.pack()

        # Botón "Agregar"
        self.boton_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_info)
        self.boton_agregar.pack()

        # Botón "Limpiar"
        self.boton_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_info)
        self.boton_limpiar.pack()

        self.boton = tk.Button(self.root, text="Enviar", command=self.enviar)
        self.boton.pack()

    def nuevo(self):
        messagebox.showinfo("Nuevo", "Función para crear un nuevo archivo")

    def abrir(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Abrir", f"Archivo abierto: {file_path}")

    def guardar(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            messagebox.showinfo("Guardar", f"Archivo guardado en: {file_path}")

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.root.quit()

    def enviar(self):
        texto = self.entrada_texto.get()
        if texto:
            messagebox.showinfo("Texto ingresado", f"El texto ingresado es: {texto}")
        else:
            messagebox.showwarning("Texto vacío", "Por favor ingrese texto antes de enviar.")

    def agregar_info(self):
        texto = self.entrada_texto.get()
        if texto:
            self.entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
            messagebox.showinfo("Información agregada", f"Se agregó: {texto} a la lista.")
            # Aquí puedes agregar la lógica para agregar el texto a una lista o tabla en la GUI
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese información antes de agregar.")

    def limpiar_info(self):
        self.entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
        # Aquí puedes agregar la lógica para limpiar la lista o tabla en la GUI

def main():
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
