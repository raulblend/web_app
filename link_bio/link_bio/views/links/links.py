import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.colors import TextColor as TextColor

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos y Redes"),
        link_button(
            "LinkedIn", 
            "Mira mi perfil!", 
            "https://www.linkedin.com/in/raul-espinoza-a320032b2/"
            ),
        link_button(
            "Script Bash", 
            "Script en Bash diseñado para automatizar el proceso de despliegue de aplicaciones en entornos de servidor.",
            "https://github.com/raulblend/deploy-script"
            ),   
        link_button(
            "Python_Reflex",
            "Página web desarrollada íntegramente en Python, utilizando el framework Reflex para crear una interfaz eficiente y dinámica!", 
            "https://github.com/raulblend/web_app"
            ),  
        link_button(
            "GitHub!",
            "Explora mis repositorios para ver ejemplos de scripts automatizados, despliegues y más. ¡no dudes en contactarme!", 
            "https://github.com/raulblend"
            ),
        width="100%",
        padding="1em"

    )