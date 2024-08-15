# fuentes de google font -> https://fonts.google.com

# Importamos reflex
import reflex as rx
# Importamos los estilos
import links.styles.styles as estilos
# Importamos los tamaños
from links.styles.styles import Size as Size
# Importamos los colores generales
from links.styles.colors import Color as Color
# Importamos los colores de los textos
from links.styles.colors import TextColor as TextColor
# Importamos las rutas
from links.routes import Router as route
# Importamos el botón flotante de la librería ant.design
from links.components.ant_components import float_button
# Importamos las constantes
import links.constants as cte

# Definimos el componente navbar
def navbar() -> rx.Component:
    # hstack: Para ver a los componentes en forma horizontal
    return rx.hstack(
        # Para poder crear un enlace que nos permita ir a otra página web
        rx.link(
            rx.box(
                rx.text.span(
                    'Iñaki ',
                    color = Color.PRIMARY.value,
                ),
                rx.text.span(
                    'Loyola',
                    color = Color.SECONDARY.value,
                ),
                style = estilos.navbar_title_style,
            ),
            # Para que regrese a la página principal
            href=route.INDEX.value
        ),
        # Añadimos el botón flotante de la librería ant.design
        float_button(
            icon = rx.image(src='/Blason.png'),
            href = cte.COFFEE_URL,
            ),
        # Posición fija
        position = 'sticky',
        # Se queda fija arriba del todo de la página web
        top='0',        
        # Color de fondo 
        bg = Color.CONTENT.value,
        # Ponemos un espacio de 16px alrededor del texto en el eje x
        padding_x = Size.BG.value,
         # Ponemos un espacio de 8px alrededor del texto en el eje y
        padding_y = Size.DF.value,
        # Para asegurarnos de que permanece en la parte superior
        z_index = '999',
    )