"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image(
                src="/photo.png",
                width="200px",
                height="auto",
                margin="0 auto",
                border_radius="15px 50px",
                border="5px solid transparent",
                background="linear-gradient(135deg, #F58529, #DD2A7B, #8134B8, #A32DB6)",
                background_clip="border-box",
                # border="5px solid #555",
            ),
            rx.heading("Welcome Raúl!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
