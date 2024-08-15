# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
from enum import Enum

# Colores principales
class Color(Enum):
    # Azul
    PRIMARY ='#14A1F0'
    # Azul oscuro
    SECONDARY = '#087ec4'
    # Azul muy muy oscuro
    BACKGROUND = '#0C151D'
    # Azul oscuro tirando a grisáceo
    CONTENT = '#171F26'

# Colores para los textos
class TextColor(Enum):
    # Cabecera - Título - Muy blanco
    HEADER = '#F1F2F4'
    # Cuerpo - Más grisáceo
    BODY = '#C3C7CB'
    # Pie - Gris más oscuro
    FOOTER = '#A3ABB2'