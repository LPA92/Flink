# Importamos reflex
import reflex as rx
# Importamos los estilos
import links.styles.styles as estilos
# Importamos las utilidades
import links.utils as utils

# Importamos los componentes que vamos a usar en la página principal
from links.components.navbar import navbar
from links.components.footer import footer
from links.views.header import header
from links.views.courses_links import courses_links
from links.styles.styles import Size as Size
from links.routes import Router

@rx.page(
    # Indicamos la ruta donde acceder a la página cursos
    route=Router.COURSES.value,
    # Solo admite una cadena alfanumérica.
    title='ILB | Cursos gratis',
    description='Este es un listado con algunos cursos gratis para aprender programación',
    image='/Escudo.png',
    # meta = Permite añadir o definido en otro archivo
    meta=utils.courses_meta
)
# Añadimos los componentes que se van a ver en la página principal
def courses() -> rx.Component:
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
                # Cabecera. details=False, para ocultar parte del header
                header(details=False),
                # Enlaces
                courses_links(),
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
