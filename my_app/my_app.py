"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

from my_app import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
        (
            "How cool is this...",
            "I know right?!"
        )
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            style=style.input_style,
        ),
        rx.button("Ask", style=style.button_style),
    )


class State(rx.State):
    index: int = 0

    def increment(self):
        self.index += 1
    
    def decrement(self):
        self.index -= 1
    
    @rx.var
    def getIndex(self) -> int:
        return self.index

def counter() -> rx.Component:
    return rx.hstack(
        rx.button("-", on_click=State.decrement),
        rx.heading(State.getIndex),
        rx.button("+", on_click=State.increment),
        style=dict(marginTop="2em"),
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            counter(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
