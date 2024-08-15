# Iconos gratis -> https//fontawesome.com
# Pulsamos en la pestaña Iconos y localizamos el icono con el buscador
# En el buscador ponemos el icono a buscar y pulsamos en la flecha (buscar)
# Pulsamos gratis, seleccionamos el icono y pulsamos en la pestaña SVG
# Pulsamos en la flecha superior ( descargar archivo SVG )
# lo añadimos a la carpeta assets de nuestro proyecto


# Importamos Reflex
import reflex as rx
# Importamos las urls
import links.constants as cte

# Importamos el componente de botón con enlace
from links.components.link_button import link_button
# Importamos el estilo del title
from links.components.title import title
# Importamos los tamaños
from links.styles.styles import Size as Size
# Importamos las rutas
from links.routes import Router as route


# Creamos el componente enlaces
def index_links() -> rx.Component:
    # Colocamos los botones en forma vertical
    return rx.vstack(
        title('Comunidad'),
        # En cada link_button hay que poner el title, el body, el icono y la url definido en link_button
        link_button(
            # title
            'Cursos gratis',
            # body
            'Consulta mis tutoriales para aprender programación',
            # imagen
            '/icons/signature-solid.svg',
            # Ruta que nos lleva a la página de cursos
            route.COURSES.value,
            # Para que no se abra en una página nueva
            is_external=False,
        ),
        link_button(
            # title
            'Twith',
            # body
            'Transmisiones sobre programación de lunes a viernes',
            # imagen
            '/icons/twitch-brands-solid.svg',
            # url
            cte.TWITCH_URL
        ),
        link_button(
            # title
            'Discord',
            # body
            'El chat y los grupos de estudio de la comunidad',
            # imagen
            '/icons/discord-brands-solid.svg',
            # url
            cte.DISCORD_URL
        ),
        link_button(
            # title
            'YouTube',
            # body
            'Tutoriales sobre desarrollo de software semanales',
            # imagen
            '/icons/youtube-brands-solid.svg',
            # url
            cte.YOUTUBE_URL
        ),
        link_button(
            # title
            'YouTube [canal secundario]',
            # body
            'Emisiones en directo destacadas',
            # imagen
            '/icons/youtube-brands-solid.svg',
            # url
            cte.YOUTUBE_SECONDARY_URL
        ),       
        title('Recursos y más'),
        # En cada link_button hay que poner el title, el body y la url definido en link_button
        link_button(
            # title
            'Git y GitHub desde cero',
            # body
            'Aquí puedes comprar mi libro en formato físico y eBook',
            # imagen
            '/icons/square-gitlab-brands-solid.svg',              
            # url
            cte.GITHUB_URL
        ),
        link_button(
            # title
            'Libros recomendados',
            # body
            'Mi listado de libros sobre programación, ciencia y tecnología',
            # imagen
            '/icons/book-solid.svg',              
            # url
            cte.BOOKS_URL
        ),
        link_button(
            # title
            'Mi setup',
            # body
            'Listado con todos los elementos que uso en mi trabajo',
            # imagen
            '/icons/meetup-brands-solid.svg',             
            # url
            cte.SETUP_URL
            ),
        link_button(
            # title
            'MoureDev',
            # body
            'Mi sitio web',
            # imagen
            '/icons/blog-solid.svg',              
            # url
            cte.MOUREDEV_URL
        ),
        link_button(
            # title
            'Invitame a un café',
            # body
            '¿Quieres ayudarme a que siga creando contenido?',
            # imagen
            '/icons/mug-saucer-solid.svg',
            # url
            cte.COFFEE_URL
        ),

        title('Contacto'),
        link_button(
            # title
            'MyPublicInbox',
            # body
            'Respuesta rápida y con preferencia',
            # imagen
            '/icons/arrow-up-from-ground-water-solid.svg',              
            # url
            cte.MYPUBLICINBOX
        ),
        link_button(
            # title
            'Correo electrónico',
            # body
            'Respuesta sin preferencia',
            # imagen
            '/icons/envelope-regular.svg',              
            # url
            # cte.EMAIL,
            f'mailto:{cte.EMAIL}'
        ),
        
        # Para que todos los enlaces ocupen el 100%
        width = '100%',
        # Para separar los diferentes link_button en el eje y 
        gap = Size.L.value,      
    )