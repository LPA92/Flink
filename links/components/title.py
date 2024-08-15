# Importamos reflex
import reflex as rx
# importamos los estilos
import links.styles.styles as estilos
# Importamos los tamaños
from links.styles.styles import Size as Size

def title(text: str) -> rx.Component:
    # heading = cabecera - equivalente a H1-H2... DE HTML
    return rx.heading(
        text,
        # Definimos el tamaño del título. es una propiedad propia del componete
        size='4',
        # Ponemos el estilo definido en el archivo sytles.py
        style=estilos.title_style,
        # Ponemos un relleno a la izquierda del componente
        padding_left=Size.DF.value
    )