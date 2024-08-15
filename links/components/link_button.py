# Importamos reflex
import reflex as rx
# Importamos los estilos
import links.styles.styles as estilos
# Importamos los tamaños
from links.styles.styles import Size as Size

# Definimos el componente botón para usarlo en las diferentes vistas
# Hay que poner dos textos,( title y body ) una url y una imagen
# Ponemos por defecto que la url se habrá en una pestaña diferente


def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        # Para poner el texto dentro del botón y ocupe todo el ancho del link
        rx.button(
            # Para que coloque horizontalmente dentro del botón
           rx.hstack(
               # Para que salga la imagen dentro del botón
               rx.image(
                   src = image,
                   # Limitamos el ancho de la imagen
                   width = Size.BG.value,
                   # Limitamos la altura de la imagen
                   height = Size.BG.value,
                   # Definimos un margen para la imagen
                   margin = Size.M.value,
                   # Texto que sale si no carga la imagen
                   alt = title
               ),
               rx.vstack(
                   # Tamaño del texto definido en button_title_style
                   rx.text(title, style=estilos.button_title_style),
                   # Tamaño del texto definido en button_body_style
                   rx.text(body, style=estilos.button_body_style),
                   # Para alinear los textos al principio del párrafo
                   align_items='start',
                   # Para que esten las letras sin espacio vertical ( eje y )
                   spacing='0',
                   # Para no tener ningún margen
                   margin = Size.ZERO.value,
                   # Ponemos un relleno en el eje Y ( vertical ) en el componente botón
                   padding_y = Size.XS.value,
                   # Ponemos un relleno a la derecha del componente botón
                   padding_right = Size.XS.value,
               ),
               # Para que todos los botones ocupen el 100%              
               width = '100%',
            ),            
        ),
        # Para poner el enlace donde ira la página web
        href=url,
        # Opción para que no se abra en una página nueva.
        is_external = is_external,
        # Para que todos los botones ocupen el 100%
        width = '100%',    
    )
