import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "RaulBlend",
                size= "7",
                color="#14A1F0",
            
            ),
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"

    ),