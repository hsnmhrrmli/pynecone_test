import pynecone as pn
import random


class State(pn.State):
    count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def random(self):
        self.count = random.randint(0, 100)


def index():
    return pn.center(
        pn.vstack(
            pn.heading(State.count),
            pn.hstack(
                pn.button("Decrement", on_click=State.decrement, color_scheme="red"),
                pn.button(
                    "Randomize",
                    on_click=State.random,
                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",
                    color="white",
                ),
                pn.button("Increment", on_click=State.increment, color_scheme="green"),
            ),
            padding="1em",
            bg="#ededed",
            border_radius="1em",
            box_shadow="lg",
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
    )

app = pn.App(state=State)
app.add_page(index, title="Counter")
app.compile()