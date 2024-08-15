# Tipo de borde, 
# solido = solid, 
# puenteado = dotted, 
# doble = double

# Importamos reflex
import reflex as rx 
# Importamos la libreria datetime de python
import datetime
# Importamos los enlaces
import links.constants as cte
# Importamos los tamaños
from links.styles.styles import Size as Size
# Importamos los colores generales
from links.styles.colors import Color as Color
# Importamos los colores de los textos
from links.styles.colors import TextColor as TextColor


# Definimos el componente footer (pie de página)
def footer() -> rx.Component:
    # Colocamos los componentes de forma vertical
    return rx.vstack(
        rx.image(
            src="/Inaki.png",
            # El ancho de la imagen la fijamos en el 5% 
            width="5%",
            # El alto de la imagen la fijamos en el 15% 
            height="15%",
            # Si no carga la imagen nos sale el texto definido en alt
            alt='Logotipo de Iñaki Loyola',
            # Definimos el borde de redondeo 
            # Borde superior derecho: 1em=16px, 
            # Borde Inferior Izquierdo: 3em=48px
            border_radius="1em 3em",
            # Estilo del borde ( tamaño, tipo, color)
            border="0.3em solid #555",
            # Coloca una sombra grande alrededor de la caja
            box_shadow="lg",
        ),
        rx.link(
            # Texto que aparece en el enlace
            # datetime.date.today().year = año actual
            f'2014-{datetime.date.today().year} realizado por Iñaki Loyola Bustamante',
            # Página Web a donde nos lleva al pulsar en el enlace
            href=cte.MOUREDEV_URL,
            # Nos abre en una nueva página
            is_external=True,
            font_size = Size.S.value,
        ),
        # Colocamos el icono de hithub al lado del texto

            rx.link(
               rx.hstack(
                   rx.image(
                        src='/icons/github-brands-solid.svg',
                        height=Size.DF.value,
                        width=Size.DF.value,
                    ),
                    # Texto que nos sale en la página web   
                    rx.text(
                        'Creado con amor desde Gran Canaria',
                        # Definimos el tamaño de la letra
                        font_size = Size.S.value,
                        margin_top =Size.ZERO.value,
                    ),
                ),
            href=cte.REPO_URL,
            is_external=True
            ),
        # Coloca en el centro los diferentes componentes
        align='center',
        # No deja sepación entre los diferentes componentes
        spacing='0',

        # Especificamos el margen inferior
        margin_bottom = Size.BG.value,
        # padding_bottom = Size.BG.value,
        color = TextColor.FOOTER.value,
        # Ponemos un relleno a la derecha del componente
        padding_x = Size.XS.value,        
    )