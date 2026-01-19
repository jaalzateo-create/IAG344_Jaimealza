# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox
from controller import procesar_instruccion


def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")
    

     # Etiqueta
    tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)
    
    def process_excel(path):
    #Acceso a la hoja de datos de excel
    wb= load_workbook(path)
    #ws = wb["Datos"]
    #Recorrer todas las filas desde la fila 2 hasta la ultima fila con datos
    #for row in range(2,ws.max_row+1):
        # columna D: identificador limpio
        #ws[f"D{row}"] = clean_id(ws[f"A{row}"].value)
        # columna E: nombre completo
        #ws[f"E{row}"] = merge_name(ws[f"B{row}"].value,ws[f"C{row}"].value)
    # guarde los cambios en el mismo archivo
    wb.save(path)
    
tk.Button(root, text="Ejecutar instrucción", command=process_excel).pack(pady=20)

    # Acción del botón
    def ejecutar():
        texto = entrada.get()
        exito, mensaje = procesar_instruccion(texto)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botón 2

    tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)

    root.mainloop()
   
    
