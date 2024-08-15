# Para usar componentes de react
# Usamos la libreria https://ant.design/

import reflex as rx
from links.styles.colors import Color

# Importamos el botón flotante de react ( aparece en la parte inferior dcha de la página web)
# rx.Var = variable anónima
class FloatButton(rx.Component):
    # Libreria, siempre la misma
    library = "antd"
    # Componente a usar de la librería antd
    tag = "FloatButton"
    # Tributo para añadir una imagen al botón flotante
    icon: rx.Var[rx.el.Img]
    # Enlace donde nos envía al pulsar en el botón flotante
    href: rx.Var[str]
    # Para indicar donde queremos que se abra la url. 
    # _blank -> Para que lo abra en una nueva pestaña
    target = "_blank"
    # Para meter el aviso
    # dot: True -> Nos muestra un punto de color rojo en vez de contador
    badge = {"dot": True, "color": Color.PRIMARY.value}

# Creamos una variable para que cree el componente que hemos importado
float_button = FloatButton.create
