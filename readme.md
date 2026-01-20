# clase IA
## 😁 comandos consola
### ![python](image.png)
```
python --version
```
### [alt text](image-1.png)
```
git --version
git init
git add . (comprime archivos)
git commit -m "primer commit"
```
### ![alt text](image-5.png)
``` 
git branch -M master
git remote add origin https://github.com/jaalzateo-create/IAG344_Jaimealza.git
  git push -u origin master
```
v2
cd personal
git status
git remote:
git push
git add .
git status: para mirar que esta pendiente por actualizar
git commit -m "IAG344 V2": esto es para actualizar la informacion pero se le debe dar una version diferente
git add . :agregar los archivos
Git push: esto se utiliza para subir los archivos
```
html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>😍😍pagina Jaime</title>
</head>
<body>
<!--este es el cuerpo de la página-->
<!--  -->
    <h1> bueno dias </h1>
    <h2>esta es mi pagina</h2>
    <h3>tercer titulo </h3>
    <h4>cuarto</h4>
    <h5> quinto</h5>
    <h6> sexto</h6>
    <p>hola bebe</p>
    <br>
    <hr>
    <p>hola bebe</p>
    <br>
    <br>
    <!-- para lista ordenada il*3 -->
    <ol>
        <li>A</li>
        <li>B</li>
        <li>C</li>
    </ol>
    <!-- para lista desordenada ul*5 -->
    <ul>
        <ul>A</ul>
        <ul>B</ul>
        <ul>C</ul>
        <ul>D</ul>
        <ul>E</ul>
    </ul>
</body>
</html>
```
### para ingresar donde esta la informacion
git branch -M main
git remote add origin https://github.com/fernandogh7508/IAG344.git
git push -u origin main
git push -u origin master
```
pip list: se encarga de mirar que librerias son las que estan instaladas.
```
cd: navega entre archivos
cd.. se sale de la carpeta
python -m venv env3.14.3 sirve para crear entorno y verificar la version de python
dir: es para verificar donde se encuentra
env3.14.2\scripts\activate\:  activar entorno visual
PS C:\WINDOWS\system32> set-Executionpolicy Unrestricted este comando se utiliza para corregir el error que sale en el entorno virtual.
S: para dar el permiso para que realice la correccion.
en: con las iniciales y tabular se puede buscar la informacion
```
.gitignore: para hacer excepciones, para no subir archivos a los entornos visuales
```
Para clonar carpeta, desde consola se ingresa: 
cd PROFES 
y se da la ruta: 
git clone https://github.com/fernandogh7508/IAG344.git
```
#librerias
import re

"""
expresiones regulares en python
problemas reales: solo lo puede ver el desarrollador si esta dentro de tres comillas

"""
#codigo: solo lo puede ver el desarrollador si esta en #
print("libreria cargada correctamente")
#ejemplo1
texto="mi numero es 12345": para que tome los numeros
resultado=re.search(r"\d+",texto):esta expresion regular para que tome los numeros y los sume
print(resultado.group())
resultado=re.search(r"\D+",texto):esta expresion regular para que tome el texto
[]un corchete representa una lista
{}llave representa un diccionario
alt+shif+F: organiza las lineas como una tabla
alt+shif+rayita abajo: para duplicar la linea

```
# 👌Entrenamiento
| patron | significado    |
| ------ | -------------- |
| `\d `  | Digito         | para visualizar git |
| `\D `  | No Digito      |
| `\W `  | Letra o numero |
| `\+ `  | uno o mas      |
| `\* `  | cero o mas     |
``
```
# deactive: desactivar entorno virtual
```
html
 se utiliza para que la pagina vaya a link que nosotros le ingresamos el usuario solo ve unal githut jaime y youtube
<header class="cabecera">
        <h1>Mi sitio</h1>

        <!-- Menu de Navegacion --> se utiliza para que la pagina vaya a link que nosotros le ingresamos el usuario solo ve unal githut jaime y youtube
         <nav>
            <a href="https://unal.edu.co/">unal</a>
            <a href="https://github.com/jaalzateo-create/IAG344_Jaimealza">githut jaime</a>
            <a href="https://youtube.com/">😊youtube</a>
         </nav>
        

    </header>
```
# comentario alt+shif+A: se utiliza para comentario
# ordenar alt+shif+F: se utiliza para ordenar la plataforma.
alt + shift + a: para sacar el comentario
alt + shift + flecha: para duplicar
li*2 multiplica la etiqueta
<ol>: Lista ordenada
<ul>: Lista no ordenada
ctrl + shift + k: para eliminar una línea 
div.container y espacio o tab: autocompleta la etiqueta
alt+shift+f: organizar la tabla y organiza la identación
alt+ctrl+shift+flecha haacia abajo: selecciona varias líneas 
```
# comandos CDM
| comando | Descripcion          |
| ------- | -------------------- |
| `cd`    | cambio de directorio |
| `cd..`    | cambio de directorio |
| `dir`   | listar               |
```

```
como se declara una funcion python: def y sub recoje todo lo que no utilizo
documento1="cc.75.055.60"

def clean_id(documento):
    return re.sub(r"\D","",documento)
print(clean_id(documento1)) este codigo sirve para sacar solamente los numeros del documento 1 y las que me coloque lo que esta dentro de las comillas"".
este es el resultado 7505560
```
SE utiliza para la logica del negocio
import re
def clean_id(value):
    # elimina caracteres no numéricos de un documento
    if value is None:
        return ""
    return re.sub(r"\D", "",str(value))

```
que se le dice al programa que busque el archivo proccessor y me traiga lo que hay en Clean id
from proccessor import clean_id
```
pip install pytest: se utiliza para instalar la libreria Pytest
pip list: se utiliza para verificar las librerias.
pytest: se utiliza para verificar la version de la biblioteca.
python.exe -m pip install --uograte: aparece si no se ha actualizado la libreria a la version que deberia
ctrl+shif+P es para sacar el comando de la parte de arriba despues escribe configure user snippets y selecciona python.
y escribe el siguiente codigo.
{
	"separador de seccion python": {
		"prefix": "sep",
		"body": [
			"# =====================",
			"# ${1: PUNTO DE ENTRADA}",
			"# ====================="
				],
				"description": "Crea un separador de secciones en python"
	}
}
coloco sep tabulador en donde quiere que este
ESte codigo se utiliza para marcar mi codigo personal es un snipper
Un snippet es un fragmento pequeño de código que se usa para realizar una tarea específica.

En Python (y en programación en general), un snippet es:

Un pedacito de código

Normalmente reutilizable

Que resuelve algo concreto (imprimir algo, leer datos, hacer un cálculo, validar información, etc.)

```
 pip freeze > requirements.txt me muestra las librerias que se necesitan
 pin install openpyxl se instala la libreria openpyxl

 ```

 ```
 #Recorrer todas las filas desde la fila 2 hasta la ultima fila con datos
    for row in range(2,ws.max_row+1):
        ws[f"D{row}"] = clean_id(ws[f"A{row}"].value): esto me guarda lo de la columna A pero que me limpie la columna A en la D del libro de Excel
```
```
Html
container para agruparlas en un sola pantalla
row: sirve para dividir la pantalla en 12 columnas
ctrl+alt+shit flecha hacia abajo para copiar en varias lineas
```

```
filedialog as flg se utiliza como alias
crear un .exe
1. Instalar librerias
   `pip install pyinstaller`
2 crear el .exe
   `pyinstaller --onefile --windowed app.py`
```

```
# este codigo nos une Mision1 con Mision2 estos son los archivos que voy a pegar
# primero creo un archivo app en Mision3
# Despues pego lo que hay en el archivo app
from ui import iniciar_app
if __name__ == "__main__":
    iniciar_app()
python main.py para correr programa
se señala primero y despues busca lo señalo Ctrl+H 
```

```
## 😁 Comandos Panda

#LIBRERIAS
--
import pandas as pd #pip install pandas
--
df =pd.read_csv("./dataset.csv")
df.head(5)
--
df.describe()
--
df["favorites"]
--
df.loc[0:2]
--
df.loc[[0,1,7]]
--
df.loc[[1,7],["favorites"]]
--
df[df["favorites"]>400]
--
df[(df["favorites"]>400)&(df["mentions"]>20)]

```