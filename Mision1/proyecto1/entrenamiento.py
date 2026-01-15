#librerias
import re

"""
expresiones regulares en python
problemas reales

"""
#codigo
print("libreria cargada correctamente")
#ejemplo1
texto="mi numero es 12345"
resultado=re.search(r"\w+",texto)
print(resultado.group())
