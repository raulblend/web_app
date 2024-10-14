import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import TextColor as TextColor
def header() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/photo.png",
            width="150px",
            height="auto",
            margin="0 auto",
            border_radius="15px 50px",
            border="5px solid transparent",
            background="linear-gradient(144deg, #F58529, #DD2A7B, #8134B8, #A32DB6)",
            background_clip="border-box",
            alt="Logo personal"
                
            #border="5px solid #555",
        ),
        rx.heading("Raúl Espinoza!", size="9", align="center",
                   color= TextColor.BODY.value),
        rx.text("Devops Engineer", size="6",
                color= TextColor.BODY.value),
        rx.text("""Soy un apasionado de la tecnología con experiencia práctica en DevOps, automatización de infraestructuras, scripting en Bash, y lenguajes como Golang y Python. Cuento con la certificación Azure Fundamentals (AZ-900) y he trabajado en proyectos que fortalecen mis habilidades en DevOps, Jenkins, automatización en la nube, y scripting en Bash.
                Estoy en búsqueda de una oportunidad en un equipo dinámico, donde pueda seguir desarrollándome como DevOps Engineer y contribuir con soluciones innovadoras que optimicen la automatización y la eficiencia.""",
                color= TextColor.BODY.value),
                padding="1em"
        ),
        