import tkinter as tk
from tkinter import filedialog, messagebox

class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")

        # Crear área de texto
        self.text_area = tk.Text(self)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Vincular atajos de teclado
        self.vincular_atajos()

        # Crear menú
        self.crear_menu()

   

    def crear_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.abrir_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar_archivo)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar", command=self.cortar, accelerator="Ctrl+X")
        editmenu.add_command(label="Copiar", command=self.copiar, accelerator="Ctrl+C")
        editmenu.add_command(label="Pegar", command=self.pegar, accelerator="Ctrl+V")
        menubar.add_cascade(label="Editar", menu=editmenu)

        self.config(menu=menubar)

   
    def abrir_archivo(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]
        )
        
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                contenido = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, contenido)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

   

    def guardar_archivo(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto","*.txt"), ("Todos los archivos","*.*")]
        )

        if not filepath:
            return
        try:
            contenido = self.text_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(contenido)
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    def vincular_atajos(self):
        """Vincula los atajos de teclado para las operaciones de edición"""
        self.bind_all("<Control-x>", lambda e: self.cortar())
        self.bind_all("<Control-c>", lambda e: self.copiar())
        self.bind_all("<Control-v>", lambda e: self.pegar())

    def cortar(self):
        """Corta el texto seleccionado al portapapeles"""
        try:
            self.text_area.event_generate("<<Cut>>")
        except tk.TclError:
            pass

    def copiar(self):
        """Copia el texto seleccionado al portapapeles"""
        try:
            self.text_area.event_generate("<<Copy>>")
        except tk.TclError:
            pass

    def pegar(self):
        """Pega el contenido del portapapeles en la posición del cursor"""
        try:
            self.text_area.event_generate("<<Paste>>")
        except tk.TclError:
            pass

 
if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()