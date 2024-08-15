# enum = define un conjunto de nombres descriptivos vinculados a valores constantes
# 1rem = Tamaño de la fuente raíz, por defecto 16px
# 1em = Tamaño de la fuente del padre,si no se define el tamaño 16px.
# gap = Espacio entre dos componentes

# Importamos reflex
import reflex as rx 
# Importamos la librería enum de python
from enum import Enum
# Importamos los colores
from .colors import Color as Color
# Importamos los colores de los textos
from .colors import TextColor as TextColor
# Importamos las fuentes
from .fonts import Font as Fonts
# Importamos el peso de las fuentes
from .fonts import FontWeight as Weight

# En mayúsculas para definir que es una constante
MAX_WIDTH = '37.5em', # 1em=16px


# Hoja de estilos ( cargamos las fuentes )
SYTLESHEETS = [
    # fuente poppins
    'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap',
        # fuente confortta
    'https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap'
]


# Tamaños a aplicar en la web
class Size(Enum):
    ZERO = '0px !important'
    XXS = '0.25em',
    XS = '0.5em',
    S = '0.75em',
    DF = '1em',
    M = '1.25em',
    L = '1.50em',
    XL = '1.75em',
    XXL = '2em',
    BG = '2.25em',
    VB = '2.5em',
    EB = '2.75em'
    UB = '3em',
    
    
# Estilos Genéricos a aplicar en toda la página web
STYLE_BASE = {
    # Establecemos la fuente por defecto
    'font_family': Fonts.DEFAULT.value,
    # Definimos el peso de la fuente por defecto
    'font_weight': Weight.LIGHT.value,
    'background_color': Color.BACKGROUND.value,
    
    # Estilo para todas las cabeceras - Títulos
    rx.heading: {
        'size':'4',
        'color': TextColor.HEADER.value,
        # Fuente a utilizar
        'font_family': Fonts.TITLE.value,
        # Peso de la fuente
        'font_weight': Weight.MEDIUM.value,
    },
    
    # Todos los botones van a tener el mismo estilo
    rx.button: {
        # Para ocupar todo el ancho disponible
        'width': '100%',
        # Para ocupar toda la altura disponible
        'height':'100%',
#        'display': 'block',
#        'padding': Size.XS.value,
        'border_radius':Size.DF.value,
        # Definimos el color del texto en los botones
        'color': TextColor.HEADER.value,
        # Definimos el color de fondo de todos los botones
        'background_color': Color.CONTENT.value,
        # Si no entra en una línea, nos aparezca en dos líneas
        'white_space': 'normal',
        # Para alinear el texto al principio de la página web
        'text_align': 'start',
        
        '_hover': {
        'background_color': Color.SECONDARY.value,            
        }
    },
    
    # Todos los enlaces van a tener el mismo estilo
    rx.link: {      
        # Para quitar el subrayado del enlace
        'text_decoration': 'none',
        # Para que se quede igual al pasar el ratón encima de él
        '_hover': {},
    },
}

# Texto de la barra de navegación
# dict = Diccionario
navbar_title_style = dict(
    # Tipo de fuente
    font_family = Fonts.LOGO.value,
    # Peso de la fuente
    font_weight = Weight.MEDIUM.value,
    # Tamaño de la fuente del botón
    font_size = Size.L.value,
    color = TextColor.HEADER.value,
)

# Texto del título que especifica a un bloque de enlaces
title_style = dict(

    # El texto ocupa el 100% de la pantalla
    width = '100%',
)

# Texto del botón
# dict = Diccionario
button_title_style = dict(
    # Tipo de fuente
    font_family = Fonts.TITLE.value,
    # Peso de la fuente
    font_weight = Weight.MEDIUM.value,
    # Tamaño de la fuente del botón
    font_size = Size.L.value,
    color = TextColor.HEADER.value,
    margin_top = Size.XXS.value,
)

# cuerpo del botón
# dict = Diccionario
button_body_style = dict(
    # Peso de la fuente
    font_weight = Weight.LIGHT.value,
    # Tamaño de la fuente del botón
    font_size = Size.DF.value,
    color = TextColor.BODY.value,
    margin_buttom = Size.XXL.value,
)