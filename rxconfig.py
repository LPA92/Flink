import reflex as rx

config = rx.Config(
    app_name="links",
    # API_URL = url donde se encuentra el backend
    # CORS = el servidor define a la/s url/s del navegador que permite el acceso al backend
    cors_allowed_origins=[
        # Acceso en local del frontend al backend
        "http://localhost:3000",
        # Acceso del frontend de la página definida en producción
        "https://links-zlbo.onrender.com"
        ],
    )