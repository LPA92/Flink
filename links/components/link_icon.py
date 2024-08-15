# linkedin
# youtube
# twitter
# facebook
# instagram


# Importamos reflex
import reflex as rx 
# Importamos los tamaños
from links.styles.styles import Size as Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
           # Para poder usar una url    
    return rx.link(
         # Para colocar el icono que corresponde a la url
         rx.image(
               src = image,
               # Establecemos el ancho de la imagen
               width = Size.DF.value,
               # Definimos la altura de la imagen
               height = Size.DF.value,
               # Ponemos el texto altenativo en el parámetro alt
               alt = alt
          ),
         # Para poner el enlace donde ira la página web
         href=url,
         # Cada vez que pulsemos el botón se nos abrirá una nueva página
         is_external = True,
    )