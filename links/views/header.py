# Importamos reflex
import reflex as rx 
# Importamos los enlaces
import links.constants as cte
# Importamos la libreria datetime de python
import datetime
# Importamos link_icon
from links.components.link_icon import link_icon
# Importamos info.text
from links.components.info_text import info_text
# Importamos los tamaños
from links.styles.styles import Size as Size
# Importamos los colores generales
from links.styles.colors import Color as Color
# Importamos los colores de los textos
from links.styles.colors import TextColor as TextColor
# Importamos las fuentes
from links.styles.fonts import Font as Fonts


# Definimos la cabecera de la página web ( heaader )
def header(details = True) -> rx.Component:
    # vstack = Posiciona los componentes de forma vertical
    return rx.vstack(
        # hstack = Posiciona los componentes de forma horizontal
        rx.hstack(
            # Toma las iniciales del nombre
            rx.avatar(
                # fallback="ILB",
                size='5',
                color=TextColor.BODY.value,
                bg = Color.CONTENT.value,
                src='/ILB.png',
                padding='0.13em',
            ),
            # Vemos el texto en el navegador, debajo del avatar
            rx.vstack(
                # Componente de titulo
                rx.heading(
                    'Iñaki Loyola',
                    size = '4',
                ),
                # Componente de texto  
                rx.text(
                    '@loyola',
                    color = TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon(
                        # icono
                        '/icons/square-gitlab-brands-solid.svg',              
                        # url
                        cte.GITHUB_URL,
                        # alt = texto para cuando no cargue la icono
                        'Git Hub'
                    ),
                    link_icon(
                        # icono
                        '/icons/facebook-f-brands-solid.svg',              
                        # url
                        cte.FACEBOOK_URL,
                        # alt = texto para cuando no cargue la icono
                        'fecebook'                        
                    ),                    
                    link_icon(
                         # icono
                         '/icons/x-twitter-brands-solid.svg',             
                        # url                        
                        cte.TWITER_X_URL,
                        # alt = texto para cuando no cargue la icono
                        'X antes Twitter'                        
                    ),
                    link_icon(
                         # icono
                        '/icons/linkedin-in-brands-solid.svg',              
                        # url        
                        cte.LINKEDIN_URL,
                        # alt = texto para cuando no cargue la icono
                        'Linkedin'                        
                    ),
                    link_icon(
                         # icono
                        '/icons/instagram-brands-solid.svg',              
                        # url        
                        cte.INSTAGRAM_URL,
                        # alt = texto para cuando no cargue la icono
                        'Instagram'                        
                    ),
                    link_icon(
                         # icono
                        '/icons/tiktok-brands-solid.svg',              
                        # url        
                        cte.TIKTOK_URL,
                        # alt = texto para cuando no cargue la icono
                        'TickTok'                        
                    ),
                    link_icon(
                        '/icons/spotify-brands-solid.svg',              
                        # url        
                        cte.SPOTIFY_URL,
                        # alt = texto para cuando no cargue la icono
                        'Spotify'
                    ),
                    # Margen superior entre hstack con heading y texy
                    margin_top=Size.XXS.value
                ),
                # Los items los alineamos a la izqda de la pantalla
                align='start',
                # Sin separación entre hstack, text y heading
                spacing=Size.ZERO.value,                                 
            ),
            # Separación vertical de hstack, text y heading
            gap=Size.XL.value,
        ),
        # Creamos una condición para ocultar la descripción
        rx.cond(
            # Para poder ocultar lo que esta dentro del box
            details,
            # Para que incluya todo lo que esta dentro del box
            rx.box(     
                # Creamos una caja flexible parea alterar sus dimnensiones y llenar el espacio disponible
                rx.flex(
                    info_text(
                        f'{experience()}+',
                        ' años de experiencia',
                    ),
                    # Deja un espacio desplazando todo hacia la derecha
                    rx.spacer(),
                    info_text(
                        '100+ ',
                        'aplicaciones creadas',
                    ),
                    # Desplaza todo hacia la derecha
                    rx.spacer(),
                    info_text(
                        '1M+',
                        'seguidores',
                    ),
                    width='100%',                
                ),
                # """ Para poner el texto en varias líneas, pero en el navegador solo aparece en una única línea
                # Coloca al centro de la página web
                rx.center(
                    rx.text(
                        """Soy ingeniero técnico en electricidad. 
                        Ingeniero electrónico industrial y automática.
                        Máster en energías renovables.
                        Máster Universitario en Desarrollo de Aplicaciones y Servicios Web """,
                        color = TextColor.BODY.value               
                    ),
                ),
            ),
        ),
        # Espacio que se deja entre hstack y text
        gap=Size.BG.value,
        # Ponemos todos los textos al margén izquierdo de la pantalla
        align='center',
        # Establecemos el relleno BG establecido en styles
        padding=Size.BG.value
    )
    
# Para calcular los años de experiencia desde que empece a trabajar    
def experience() -> int:
    return datetime.date.today().year - 1987    
