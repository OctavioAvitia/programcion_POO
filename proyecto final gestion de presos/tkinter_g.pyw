import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

# Conexión a la base de datos de MySQL
try:
    conecction = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_de_presos"
    )
    cursor = conecction.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
    exit()

# Función para validar las credenciales
def validar_credenciales(usuario, contraseña):
    query = "SELECT * FROM usuarios WHERE user = %s AND con = %s"
    cursor.execute(query, (usuario, contraseña))
    resultado = cursor.fetchone()
    return resultado is not None

# Función para manejar el evento de inicio de sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if validar_credenciales(usuario, contraseña):
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        ventana.withdraw()  # Ocultar la ventana de inicio de sesión
        abrir_menu_principal()  # Abrir la pantalla del menú principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para abrir el menú principal con opciones
def abrir_menu_principal():
    menu_ventana = tk.Toplevel()
    menu_ventana.title("Menú Principal")
    menu_ventana.geometry("300x350")

    btn_presos = tk.Button(menu_ventana, text="Presos", command=abrir_gestion_presos)
    btn_presos.pack(pady=10)

    btn_crimen = tk.Button(menu_ventana, text="Crimen", command=abrir_gestion_crimenes)
    btn_crimen.pack(pady=10)

    btn_guardias = tk.Button(menu_ventana, text="Guardias", command=abrir_gestion_guardias)
    btn_guardias.pack(pady=10)

    btn_celda = tk.Button(menu_ventana, text="Celda", command=abrir_gestion_celdas)
    btn_celda.pack(pady=10)

    btn_salir = tk.Button(menu_ventana, text="Salir", command=lambda: salir(menu_ventana))
    btn_salir.pack(pady=10)

# Función para abrir la ventana de gestión de presos
def abrir_gestion_presos():
    gestion_ventana = tk.Toplevel()
    PresoApp(gestion_ventana)

# Función para abrir la ventana de gestión de celdas
def abrir_gestion_celdas():
    gestion_ventana = tk.Toplevel()
    CeldaApp(gestion_ventana)

# Función para abrir la ventana de gestión de crímenes
def abrir_gestion_crimenes():
    gestion_ventana = tk.Toplevel()
    CrimenApp(gestion_ventana)

# Función para abrir la ventana de gestión de guardias
def abrir_gestion_guardias():
    gestion_ventana = tk.Toplevel()
    GuardiasApp(gestion_ventana)

# Función para salir y regresar a la pantalla de inicio de sesión
def salir(ventana_actual):
    ventana_actual.destroy()
    ventana.deiconify()

class PresoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Presos")
        self.root.geometry("500x400")

        # Crear un frame para la lista de presos
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Crear la tabla (Treeview) para mostrar la lista de presos
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Años Cárcel", "Zona Celda", "Crimen"), show="headings", height=8)
        self.tree.pack()

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Años Cárcel", text="Años Cárcel")
        self.tree.heading("Zona Celda", text="Zona Celda")
        self.tree.heading("Crimen", text="Crimen")

        self.actualizar_lista()

        # Botones de acción
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        btn_registrar = tk.Button(btn_frame, text="Registrar", command=self.registrar)
        btn_registrar.grid(row=0, column=0, padx=10)

        btn_editar = tk.Button(btn_frame, text="Editar", command=self.editar)
        btn_editar.grid(row=0, column=1, padx=10)

        btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=self.eliminar)
        btn_eliminar.grid(row=0, column=2, padx=10)

        btn_consultar = tk.Button(btn_frame, text="Consultar", command=self.actualizar_lista)
        btn_consultar.grid(row=0, column=3, padx=10)

        # Botón para regresar a la pantalla de inicio de sesión
        btn_salir = tk.Button(root, text="Salir", command=self.salir)
        btn_salir.pack(pady=10)

    def actualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        cursor.execute("SELECT * FROM preso")
        Mostrar = cursor.fetchall()

        for fila in Mostrar:
            self.tree.insert("", "end", values=fila)

    def registrar(self):
        self.formulario("Registrar Preso", self.guardar_registro)

    def guardar_registro(self, Nombre, Años_carcel, Zona_Celda, Crimen):
        query = "INSERT INTO preso (Nombre,Años_Carcel,Zona_Celda,Crimen) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (Nombre, Años_carcel, Zona_Celda, Crimen))
        conecction.commit()
        messagebox.showinfo("Éxito", "Registro realizado correctamente.")
        self.actualizar_lista()

    def editar(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado)
            id = item["values"][0]
            self.formulario("Editar Preso", lambda Nombre, Años_carcel, Zona_Celda, Crimen: self.guardar_edicion(id, Nombre, Años_carcel, Zona_Celda, Crimen), item["values"][1:])
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un preso para editar.")

    def guardar_edicion(self, id, Nombre, Años_carcel, Zona_Celda, Crimen):
        comando = "UPDATE preso SET Nombre=%s, Años_Carcel=%s, Zona_Celda=%s, Crimen=%s WHERE id = %s"
        cursor.execute(comando, (Nombre, Años_carcel, Zona_Celda, Crimen, id))
        conecction.commit()
        messagebox.showinfo("Éxito", "Edición realizada correctamente.")
        self.actualizar_lista()

    def eliminar(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado)
            id = item["values"][0]
            borrar = f"DELETE FROM preso WHERE id = {id}"
            cursor.execute(borrar)
            conecction.commit()
            messagebox.showinfo("Éxito", "Preso eliminado correctamente.")
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un preso para eliminar.")

    def formulario(self, titulo, guardar_callback, valores=None):
        form = tk.Toplevel(self.root)
        form.title(titulo)

        tk.Label(form, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(form)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form, text="Años Cárcel:").grid(row=1, column=0, padx=10, pady=10)
        entry_años = tk.Entry(form)
        entry_años.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form, text="Zona Celda:").grid(row=2, column=0, padx=10, pady=10)
        entry_zona = tk.Entry(form)
        entry_zona.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(form, text="Crimen:").grid(row=3, column=0, padx=10, pady=10)
        entry_crimen = tk.Entry(form)
        entry_crimen.grid(row=3, column=1, padx=10, pady=10)

        if valores:
            entry_nombre.insert(0, valores[0])
            entry_años.insert(0, valores[1])
            entry_zona.insert(0, valores[2])
            entry_crimen.insert(0, valores[3])

        btn_guardar = tk.Button(form, text="Guardar", command=lambda: [guardar_callback(entry_nombre.get(), entry_años.get(), entry_zona.get(), entry_crimen.get()), form.destroy()])
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def salir(self):
        self.root.destroy()
        ventana.deiconify()
class CeldaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Celdas")
        self.root.geometry("400x300")

        # Crear un frame para la lista de celdas
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Crear la tabla (Treeview) para mostrar la lista de celdas
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Zona", "Capacidad"), show="headings", height=8)
        self.tree.pack()

        self.tree.heading("ID", text="ID")
        self.tree.heading("Zona", text="Zona")
        self.tree.heading("Capacidad", text="Capacidad")

        self.actualizar_lista()

        # Botones de acción
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        btn_registrar = tk.Button(btn_frame, text="Registrar", command=self.registrar)
        btn_registrar.grid(row=0, column=0, padx=10)

        btn_editar = tk.Button(btn_frame, text="Editar", command=self.editar)
        btn_editar.grid(row=0, column=1, padx=10)

        btn_eliminar = tk.Button(btn_frame, text="Eliminar", command=self.eliminar)
        btn_eliminar.grid(row=0, column=2, padx=10)

        btn_consultar = tk.Button(btn_frame, text="Consultar", command=self.actualizar_lista)
        btn_consultar.grid(row=0, column=3, padx=10)

        # Botón para regresar a la pantalla de inicio de sesión
        btn_salir = tk.Button(root, text="Salir", command=self.salir)
        btn_salir.pack(pady=10)

    def actualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        cursor.execute("SELECT * FROM celdas")
        Mostrar = cursor.fetchall()

        for fila in Mostrar:
            self.tree.insert("", "end", values=fila)

    def registrar(self):
        self.formulario("Registrar Celda", self.guardar_registro)

    def guardar_registro(self, Zona, Capacidad):
        query = "INSERT INTO celdas (Zona, Capacidad) VALUES (%s,%s)"
        cursor.execute(query, (Zona, Capacidad))
        conecction.commit()
        messagebox.showinfo("Éxito", "Registro realizado correctamente.")
        self.actualizar_lista()

    def editar(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado)
            id = item["values"][0]
            self.formulario("Editar Celda", lambda Zona, Capacidad: self.guardar_edicion(id, Zona, Capacidad), item["values"][1:])
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una celda para editar.")

    def guardar_edicion(self, id, Zona, Capacidad):
        comando = "UPDATE celdas SET Zona=%s, Capacidad=%s WHERE id = %s"
        cursor.execute(comando, (Zona, Capacidad, id))
        conecction.commit()
        messagebox.showinfo("Éxito", "Edición realizada correctamente.")
        self.actualizar_lista()

    def eliminar(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado)
            id = item["values"][0]
            borrar = f"DELETE FROM celdas WHERE id = {id}"
            cursor.execute(borrar)
            conecction.commit()
            messagebox.showinfo("Éxito", "Celda eliminada correctamente.")
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una celda para eliminar.")

    def formulario(self, titulo, guardar_callback, valores=None):
        form = tk.Toplevel(self.root)
        form.title(titulo)

        tk.Label(form, text="Zona:").grid(row=0, column=0, padx=10, pady=10)
        entry_zona = tk.Entry(form)
        entry_zona.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form, text="Capacidad:").grid(row=1, column=0, padx=10, pady=10)
        entry_capacidad = tk.Entry(form)
        entry_capacidad.grid(row=1, column=1, padx=10, pady=10)

        if valores:
            entry_zona.insert(0, valores[0])
            entry_capacidad.insert(0, valores[1])

        btn_guardar = tk.Button(form, text="Guardar", command=lambda: [guardar_callback(entry_zona.get(), entry_capacidad.get()), form.destroy()])
        btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)

    def salir(self):
        self.root.destroy()
        ventana.deiconify()
def abrir_gestion_celdas():
    gestion_ventana = tk.Toplevel()
    app = CeldaApp(gestion_ventana)

class CrimenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Crímenes")
        self.crimen = "Crimen"

        # Crear los botones para las diferentes opciones
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Acción a realizar en la tabla:", font=('Arial', 16)).pack(pady=10)

        tk.Button(self.root, text="Registrar", width=20, command=self.registrar).pack(pady=5)
        tk.Button(self.root, text="Editar", width=20, command=self.editar).pack(pady=5)
        tk.Button(self.root, text="Eliminar", width=20, command=self.eliminar).pack(pady=5)
        tk.Button(self.root, text="Consultar", width=20, command=self.consulta).pack(pady=5)
        tk.Button(self.root, text="Salir", width=20, command=self.root.quit).pack(pady=20)

    def registrar(self):
        Tipo_Crimen = simpledialog.askstring("Registro", "Ingrese el crimen cometido:")
        Condena_Crimen = simpledialog.askstring("Registro", "Ingrese la condena que se le dará:")
        Zona_Celda = simpledialog.askinteger("Registro", "Ingrese la ubicación a la que va (ingrese número de zona):")
        
        if Tipo_Crimen and Condena_Crimen and Zona_Celda is not None:
            query = "INSERT INTO crimenes (Tipo_Crimen, Condena_Crimen, Zona_Celda) VALUES (%s, %s, %s)"
            cursor.execute(query, (Tipo_Crimen, Condena_Crimen, Zona_Celda))
            conecction.commit()
            messagebox.showinfo("Éxito", "Se realizó correctamente el registro.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def editar(self):
        id = simpledialog.askstring("Editar", "Ingrese el ID del crimen a editar:")
        cursor.execute("SELECT * FROM crimenes WHERE id = %s;", (id,))
        resultado = cursor.fetchone()

        if resultado:
            Tipo_Crimen = simpledialog.askstring("Editar", f"El tipo de crimen es {resultado[1]}. Ingrese el nuevo crimen:")
            Condena_Crimen = simpledialog.askstring("Editar", f"La condena actual es {resultado[2]}. Ingrese la nueva condena:")
            Zona_Celda = simpledialog.askinteger("Editar", f"La zona actual es {resultado[3]}. Ingrese la nueva zona:")

            comando = "UPDATE crimenes SET Tipo_Crimen=%s, Condena_Crimen=%s, Zona_Celda=%s WHERE id=%s"
            cursor.execute(comando, (Tipo_Crimen, Condena_Crimen, Zona_Celda, id))
            conecction.commit()
            messagebox.showinfo("Éxito", "Edición completada.")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un crimen con ese ID.")

    def eliminar(self):
        id = simpledialog.askstring("Eliminar", "Ingrese el ID del crimen a eliminar:")
        comando = "DELETE FROM crimenes WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        messagebox.showinfo("Éxito", "Se eliminó exitosamente.")

    def consulta(self):
        cursor.execute("SELECT * FROM crimenes")
        Mostrar = cursor.fetchall()
        consulta_resultado = ""
        
        if Mostrar:
            for fila in Mostrar:
                consulta_resultado += f"ID: {fila[0]}\nTipo de Crimen: {fila[1]}\nCondena: {fila[2]}\nZona: {fila[3]}\n\n"
        else:
            consulta_resultado = "No hay datos disponibles."

        messagebox.showinfo("Consulta", consulta_resultado)

class GuardiasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Guardias")
        self.guardia = "Guardias"

        # Crear los botones para las diferentes opciones
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Acción a realizar en la tabla:", font=('Arial', 16)).pack(pady=10)

        tk.Button(self.root, text="Registrar", width=20, command=self.registrar).pack(pady=5)
        tk.Button(self.root, text="Editar", width=20, command=self.editar).pack(pady=5)
        tk.Button(self.root, text="Eliminar", width=20, command=self.eliminar).pack(pady=5)
        tk.Button(self.root, text="Consultar", width=20, command=self.consulta).pack(pady=5)
        tk.Button(self.root, text="Salir", width=20, command=self.root.quit).pack(pady=20)

    def registrar(self):
        Nombre = simpledialog.askstring("Registro", "Ingrese el nombre del guardia:")
        Zona_Asig = simpledialog.askstring("Registro", "Ingrese la zona asignada:")
        Turno = simpledialog.askstring("Registro", "Ingrese el turno de trabajo:")
        
        if Nombre and Zona_Asig and Turno:
            query = "INSERT INTO guardias (Nombre, Zona_Asig, Turno) VALUES (%s, %s, %s)"
            cursor.execute(query, (Nombre, Zona_Asig, Turno))
            conecction.commit()
            messagebox.showinfo("Éxito", "Se realizó correctamente el registro.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def editar(self):
        id = simpledialog.askstring("Editar", "Ingrese el ID del guardia a editar:")
        cursor.execute("SELECT * FROM guardias WHERE id = %s;", (id,))
        resultado = cursor.fetchone()

        if resultado:
            Nombre = simpledialog.askstring("Editar", f"Nombre actual: {resultado[1]}. Ingrese el nuevo nombre:")
            Zona_Asig = simpledialog.askstring("Editar", f"Zona actual: {resultado[2]}. Ingrese la nueva zona:")
            Turno = simpledialog.askstring("Editar", f"Turno actual: {resultado[3]}. Ingrese el nuevo turno:")

            comando = "UPDATE guardias SET Nombre = %s, Zona_Asig = %s, Turno = %s WHERE id = %s"
            cursor.execute(comando, (Nombre, Zona_Asig, Turno, id))
            conecction.commit()
            messagebox.showinfo("Éxito", "Edición completada.")
        else:
            messagebox.showwarning("Advertencia", "No se encontró un guardia con ese ID.")

    def eliminar(self):
        id = simpledialog.askstring("Eliminar", "Ingrese el ID del guardia a eliminar:")
        comando = "DELETE FROM guardias WHERE id = %s"
        cursor.execute(comando, (id,))
        conecction.commit()
        messagebox.showinfo("Éxito", "Se eliminó exitosamente.")

    def consulta(self):
        cursor.execute("SELECT * FROM guardias")
        Mostrar = cursor.fetchall()
        consulta_resultado = ""
        
        if Mostrar:
            for fila in Mostrar:
                consulta_resultado += f"ID: {fila[0]}\nNombre: {fila[1]}\nZona: {fila[2]}\nTurno: {fila[3]}\n\n"
        else:
            consulta_resultado = "No hay datos disponibles."

        messagebox.showinfo("Consulta", consulta_resultado)

# Interfaz de inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("300x200")

tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

btn_iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
btn_iniciar_sesion.pack(pady=20)

ventana.mainloop()
