# Importamos reflex
import reflex as rx
# Importamos los tamaños
from links.styles.styles import Size as Size
# Importamos las fuentes
from links.styles.fonts import Font as Fonts
# Importamos los pesos de las fuentes
from links.styles.fonts import FontWeight as Weight
# Importamos los colores generales
from links.styles.colors import Color as Color
# Importamos los colores para los textos
from links.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        # chakra.span es la única forma de poner un span en reflex
        # span para definir unas características propias diferentes del resto
        rx.text.span(
            title,
            # Definimos el tipo de fuente
            font_family=Fonts.TITLE.value,
            # Definimos el peso de la fuente
            font_weight=Weight.MEDIUM.value,
            # Establecemos el color de la fuente para el span
            color=Color.PRIMARY.value,
        ),
        f' {body}',
        # Definimos el tamaño de la fuente para todo lo que contiene el box
        font_size=Size.S.value,
        # Establecemos el color del texto del box excepto para el span
        color = TextColor.BODY.value,
    )
