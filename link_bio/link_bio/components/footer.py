import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            f"2022-{datetime.date.today().year} by Raulblend",
            href="https://www.linkedin.com/in/raul-espinoza-a320032b2/",
            is_external=True
        ),
        rx.logo(),
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )