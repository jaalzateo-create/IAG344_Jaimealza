esta es la ruta para python 3.13.3
C:\Users\Jaime\AppData\Local\Programs\Python\Python313\python.exe
De esta manera se instala la version 3.13.3 de python siguinedo esta ruta porque la vamos a trabajar en la version 13.3
PS C:\Guia talento tech\personal> cd .\Mision3\
PS C:\Guia talento tech\personal\Mision3> C:\Users\Jaime\AppData\Local\Programs\Python\Python313\python.exe -m venv venv3.13
PS C:\Guia talento tech\personal\Mision3> venv3.13\scripts\activate
(venv3.13) PS C:\Guia talento tech\personal\Mision3>

(venv3.13) PS C:\Guia talento tech\personal\Mision3> pip install -r requirements.txt: se utiliza para actualizar el requiremnents de version1

from sklearn.feature_extraction.text import CountVectorizer: estas librerias convierte el texto en un vector.
from sklearn.naive_bayes import MultinomialNB: libreria entiende un texto y libreria exclusiva de inteligencia artificial.
 user_input = input("Tú: ").strip(): la funcion strip elimina los espacios adelante y atras del texto

python chatbot_sp.py: con esta funcion en python se corre el chatbot para generar lo que se necesita