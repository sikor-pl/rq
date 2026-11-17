from collections.abc import Callable

import flet as ft


def build_page(on_next: Callable[[], None]) -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Etap 4 - żółty krzyż", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Kolejny etap. Trzymamy teraz kostkę żółtym do góry - jak na obrazkach. Naszym zadaniem jest ułożenie na górnej ściance żółtego krzyża."),
            ft.Image(
                src="zolty_krzyz_3.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text("Dodaj do assets: zolty_krzyz_3.gif"),
            ),
            ft.Text("Sekwencja 1", size=24, weight=ft.FontWeight.BOLD),
            # ft.Text("Miejsce na opis pierwszej sekwencji."),
            ft.Image(
                src="zolty_krzyz_1.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text("Dodaj do assets: zolty_krzyz_1.gif"),
            ),
            ft.Text("Sekwencja 2", size=24, weight=ft.FontWeight.BOLD),
            ft.Image(
                src="zolty_krzyz_2.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text("Dodaj do assets: zolty_krzyz_2.gif"),
            ),
            ft.Button(
                content="Etap 5 - permutacja żółtego krzyża",
                icon=ft.Icons.ARROW_FORWARD,
                on_click=on_next,
            ),
        ],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
