# Importamos reflex
import reflex as rx
# Importamos los estilos
import links.styles.styles as estilos
# Importamos las utilidades
import links.utils as utils

# Importamos los componentes que vamos a usar en la página principal
# Página de navegación
from links.components.navbar import navbar
# Cabecera
from links.views.header import header
# Pie de página
from links.components.footer import footer

# Enlaces de la página index
from links.views.index_links import index_links
# Importamos los tamaños
from links.styles.styles import Size as Size

# Estamos definiendo que el archivo index.py es una página de la web
@rx.page(
    # Solo admite una cadena alfanumérica.
    title = 'ILB',
    description='Hola, mi nombre es Iñaki Loyola. Soy Ingeniero electrónico Industrial y Automática',
    image='/Escudo.png',
    # meta = Permite añadir o definido en otro archivo
    meta = utils.index_meta
)

# Añadimos los componentes que se van a ver en la página principal
def index() -> rx.Component:
    # box: Contenedor genérico que se utiliza para usar otros contenedores
    return rx.box(
        # Idioma de la página
        utils.lang(),
        # Navegación
        navbar(),
        # Para centrar los componentes que hay en vstack
        rx.center(
            # Para colocar verticalmente los componentes
            rx.vstack(
                # Cabecera
                header(),
                # Enlaces
                index_links(),
                # Limitamos el ancho de la página a 37,5em definido en sytles.py
                max_width=estilos.MAX_WIDTH,
                # Para que ocupe el 100% lo que hay dentro del vstack
                width='100%',
                # dejamos un margen de 1.25em en el eje y
                margin_y=Size.XXL,
            ),
        ),
        # Pie de página
        footer(),
    )
