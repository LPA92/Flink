# Despliegue de la página web
# https://reflex.dev/docs/hosting/deploy-quick-start/#reflex-hosting-service
# reflex login -> darse de alta usando gmail
# reflex deploy
# -> Nos pide el nombre del proyecto
# -> Región -> mad
# -> Variables de entorno -> no

# Para que nos empaquete el frontend -> sh build.sh

# Activar el entorno virtual    -> python3.12 -m venv .virtual
#                               -> source .virtual/bin/activate
# Desactivar el entorno virtual -> deactivate

# rx.text(
#    "This is a ",
#    rx.text.strong("span"),    dentro va el span
#    " element.",
#    as_="span",
# ),


"""Bienvenido a Reflex"""

# Importamos reflex
import reflex as rx
# Importamos los estilos
import links.styles.styles as estilos

# Importamos la página index
from links.pages.index import index
# Importamos la página courses
from links.pages.courses import courses

class State(rx.State):
    ### Define tu bakend aqui ###
 ...

# Crea una aplicación con Reflex
app = rx.App(
    # Nos coge todos los estilos base definidos en STYLESHEETS
    stylesheets=estilos.SYTLESHEETS,
    # Nos coge todos los estilos base definidos en STYLE_BASE
    style=estilos.STYLE_BASE
)



