from collections.abc import Callable

import flet as ft


def illustration(filename: str) -> ft.Image:
    return ft.Image(
        src=filename,
        fit=ft.BoxFit.CONTAIN,
        error_content=ft.Text(f"Dodaj do assets: {filename}"),
    )


def build_page(on_next: Callable[[], None] | None = None) -> ft.Control:
    controls = [
            ft.Text(
                "Etap 5 - permutacja żółtego krzyża",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text(
                "Na tym etapie trzymamy żółtą ściankę u góry (nie do siebie przodem). Co mamy teraz uzyskać:"
            ),
            illustration("permutacja_zoltego_krzyza_1.gif"),
            ft.Text(
                "Kręcimy górną ścianką tak długo, aż napotkamy jeden z trzech poniższych przypadków:"
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        width=168,
                        content=ft.Column(
                            controls=[
                                illustration(f"permutacja_zoltego_krzyza_{number}.gif"),
                                ft.Text(description),
                            ],
                            spacing=4,
                        ),
                    )
                    for number, description in (
                        (21, "Wszystkie żółte ramiona krzyża ustawione prawidłowo - nic nie robimy - przechodzimy do kolejnego etapu."),
                        (22, "Dwa ramiona obok siebie ustawione prawidłowo. Wykonujemy algorytm 1 raz."),
                        (23, "Dwa ramiona naprzeciwko siebie ustawione prawidłowo. Wykonujemy algorytm 2 razy, ale po pierwszym wykonaniu ustawiamy kostkę tak jak w przypadku nr 2."),
                    )
                ],
                wrap=True,
                spacing=8,
                run_spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            illustration("permutacja_zoltego_krzyza_a.gif"),
            ft.Text(
                """Jeśli napotkamy przypadek drugi, ustawiamy kostkę tak, aby prawidłowo spermutowane żółte klocki znalazły się z przodu i z lewej strony (białe kropki) i wykonujemy algorytm. Po wykonaniu algorytmu dokręcamy górną ściankę 1 raz aby prawidłowo ustawić klocki na miejscach.

Jeśli napotkamy sytuację trzecią, gdzie dwa klocki są prawidłowe ale naprzeciwko siebie (białe kropki), ustawiamy jeden na górze, a drugi na dole i wykonujemy algorytm. Po jego wykonaniu ustawiamy kostkę jak w sytuacji drugiej czyli ustawiamy dobre klocki na dole i po lewej i wykonujemy algorytm ponownie. Po drugim wykonaniu algorytmu dokręcamy górną ścianę dopasowując kolory.
Kolejny etap"""
            ),
        ]
    if on_next is not None:
        controls.append(
            ft.Button(
                content="Etap 6 - permutacja narożników",
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
