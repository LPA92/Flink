# fuentes de google font -> https://fonts.google.com

# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
from enum import Enum

# Clase de fuente a usar
class Font(Enum):
    DEFAULT = 'Poppins'
    TITLE = ' Poppins'
    LOGO = 'Comfortaa'

# Anchura de la fuente
class FontWeight(Enum):
     LIGHT = '300'         # Letra normal
     MEDIUM = '500'        # Letra negrita
    