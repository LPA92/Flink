# Para usarlo como numeral
from enum import Enum

# Clase donde se definen los diferentes enlaces que nos llevan a las diferentes páginas web que contiene nuestra web
class Router(Enum):
    INDEX = '/'
    COURSES = '/cursos'