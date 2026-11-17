from collections.abc import Callable

import flet as ft


def illustration(filename: str) -> ft.Image:
    return ft.Image(
        src=filename,
        fit=ft.BoxFit.CONTAIN,
        error_content=ft.Text(f"Dodaj do assets: {filename}"),
    )


def image_slot(key: str, filename: str) -> ft.Container:
    return ft.Container(key=key, content=illustration(filename))


def description_slot(key: str) -> ft.Container:
    return ft.Container(key=key, content=ft.Text("Miejsce na opis"))


def build_page(on_next: Callable[[], None] | None = None) -> ft.Control:
    controls = [
        ft.Text(
            "Etap 6 — permutacja narożników",
            size=32,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text("""Etap ten zawiera algorytmy umożliwiające ustawienie 4 żółtych narożników na swoich miejscach.
Na początek ważna uwaga: narożnik na swoim miejscu nie oznacza, że jest on prawidłowo zorientowany (przekręcony), może być, ale nie musi, a i tak jest na swoim miejscu. Oznacza to, że klocek znajduje się w miejscu kostki, gdzie pozostanie już do końca tylko potem należy go jeszcze przekręcić wg jego własnej osi. Poniżej przykłady ustawień klocka na swoim miejscu:"""),
        image_slot(
            "corner-permutation-introduction",
            "permutacja_naroznikow_1.gif",
        ),
        description_slot("corner-permutation-introduction-description"),
        ft.Text("""W pierwszych trzech przypadkach klocek narożny jest na swoim miejscu, ponieważ znajduje się na ścianie żółto-czerwono-zielonej. W czwartym przypadku klocek nie jest na swoim miejscu, ponieważ powinien znaleźć się na ścianie żółto-niebiesko-pomarańczowej.


Na początek obrazek przedstawiający co mamy uzyskać w tym kroku:"""),
        image_slot(
            "corner-permutation-position-example",
            "permutacja_naroznikow_2.gif",
        ),
        description_slot("corner-permutation-position-example-description"),
        ft.Text("""Jak widzimy na powyższym obrazku, narożnik żółto-czerwono-zielony (zaznaczony kropką) jest już na swoim miejscu, natomiast pozostałe 3 narożniki nie są na swoich miejscach. Na obrazku po prawej widzimy, że klocek żółto-zielono-czerwony pozostał na swoim miejscu, natomiast trzy pozostałe zostały przestawione na swoje miejsca.

Występują tutaj dwa przypadki algorytmu.
Pierwszy z nich to permutacja trzech narożników w prawo, czyli zgodnie ze wskazówkami zegara. Ustawiamy kostkę tak, aby żółty krzyż był na górnej ścianie, a klocek, który nie powinien zmieniać swojego położenia musi być tam gdzie zaznaczono kropką (rys. trzeci poniżej):
"""),
        image_slot(
            "corner-permutation-right-algorithm",
            "permutacja_naroznikow_3.gif",
        ),
        description_slot("corner-permutation-right-algorithm-description"),
        ft.Text("""Drugim przypadkiem jest permutacja trzech narożników w lewo, czyli odwrotnie do wskazówek zegara. Ustawiamy kostkę tak, aby żółty krzyż był na górnej ścianie, a klocek, który nie powinien zmieniać swojego położenia musi być tam gdzie zaznaczono kropką (rys. trzeci poniżej):"""),
        image_slot(
            "corner-permutation-left-algorithm",
            "permutacja_naroznikow_4.gif",
        ),
        description_slot("corner-permutation-left-algorithm-description"),
        ft.Text("Jeżeli zdarzy nam się przypadek, że ŻADEN z narożników nie będzie na swoim miejscu musimy najpierw wykonać jakikolwiek z powyższych algorytmów, następnie poszukać jednego klocka który znalazł się na swoim miejscu i wykonać ponownie odpowiedni algorytm."),
        ft.Text("Po zakończeniu tego etapu przechodzimy do kolejnego."),
    ]
    if on_next is not None:
        controls.append(
            ft.Button(
                content="Etap 7 - orientacja narożników",
                icon=ft.Icons.ARROW_FORWARD,
                on_click=on_next,
            )
        )

    return ft.Column(
        controls=controls,
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
