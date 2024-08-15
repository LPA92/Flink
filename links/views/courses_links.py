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


# Creamos el componente enlaces
def courses_links() -> rx.Component:
    # Colocamos los botones en forma vertical
    return rx.vstack(
        title('Cursos gratis'),
        # En cada link_button hay que poner el title, el body, el icono y la url definido en link_button
        link_button(
            # title
            'Retos de programación',
            # body
            'Ruta de estudio semanal para practicar lógica de programación',
            # imagen
            '/challenges.png',
            # Ruta que nos lleva a la página de cursos
            cte.CODE_CHALLENGES_URL,
        ),
        link_button(
            # title
            'Python desde cero',
            # body
            'Curso de +37h: Fundamentos, frontend, backend, testing........',
            # imagen
            '/icons/python-brands-solid.svg',
            # Ruta que nos lleva a la página de cursos
            cte.PYTHON_COURSE_URL,
        ),
        link_button(
            # title
            'Git y GitHUb',
            # body
            'Curso de 5 horas para aprender Git y GitHub desde cero',
            # imagen
            '/icons/github-brands-solid.svg',
            # Ruta que nos lleva a la página de cursos
            cte.GITHUB_URL,
        ),
        link_button(
            # title
            'SQL y base de datos',
            # body
            'Curso de 7h desde cero para aprender los fundamentos de SQL',
            # imagen
            '/icons/database-solid.svg',
            # Ruta que nos lleva a la página de cursos
            cte.SQL_COURSE_URL,
        ),
        link_button(
            # title
            'Un día, un lenguaje',
            # body
            'Primeros pasos en los 11 lenguajes de programación más usados',
            # imagen
            '/icons/laptop-code-solid.svg',
            # Ruta que nos lleva a la página de cursos
            cte.LANGUAGES_COURSE_URL,
        ),
        title('Mucho más en'),
        link_button(
            # title
            "Twitch",
            # body
            'Transmisiones sobre programación de lunes a viernes',
            # icono
            '/icons/facebook-f-brands-solid.svg',
            # url
            cte.TWITCH_URL,
        ),
        link_button(
            # title
            'Discord',
            # body
            'El chat y los grupos de estudio de la comunidad',
            # icono
            '/icons/discord-brands-solid.svg',
            # url
            cte.TWITER_X_URL,
        ),
        link_button(
            # title
            'Youtube',
            # body
            'Tutoriales sobre desarrollo de sottware semanales',
            # icono
            '/icons/youtube-brands-solid.svg',
            # url
            cte.YOUTUBE_URL,
        ),
        link_button(
            # title
            'Youtube [canal secundario]',
            # body
            'Emisiones en directo destacados',
            # icono
            '/icons/youtube-brands-solid.svg',
            # url
            cte.YOUTUBE_SECONDARY_URL,
        ),
        # Para que todos los enlaces ocupen el 100%
        width = '100%',
        # Para separar los diferentes link_button en el eje y 
        gap = Size.L.value,      
    )