from collections.abc import Callable

import flet as ft


def image(filename: str) -> ft.Image:
    return ft.Image(
        src=filename,
        fit=ft.BoxFit.CONTAIN,
        error_content=ft.Text(f"Dodaj do assets: {filename}"),
    )


def build_page(on_next: Callable[[], None] | None = None) -> ft.Control:
    cases = (
        (
            "auto",
            "Auto",
            "Dwa żółte pola wskazują ten sam kierunek, tworząc układ przypominający reflektory auta. Ustaw kostkę jak na rysunku i zacznij od algorytmu w prawo.",
        ),
        (
            "zaba",
            "Żaba",
            "Dwa żółte pola po przeciwnych stronach przypominają oczy żaby. Ustaw kostkę jak na ilustracji i wykonaj algorytm w prawo.",
        ),
        (
            "2zle",
            "Dwa źle po przekątnej",
            "Dwa źle zorientowane narożniki leżą po przekątnej. Trzymając kostkę jak na rysunku, wykonaj algorytm w prawo.",
        ),
        (
            "2auta",
            "Dwa auta",
            "Dwie pary żółtych pól tworzą układ reflektorów po bokach. Ustaw kostkę tak, aby pary były skierowane w lewo i w prawo.",
        ),
        (
            "zabaplusauto",
            "Żaba i auto",
            "Ten układ łączy wzór żaby z autem. Ustaw kostkę jak na ilustracji, z reflektorami skierowanymi ku sobie.",
        ),
    )

    controls = [
        ft.Text(
            "Etap 7 — orientacja narożników",
            size=32,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text(
            """Celem tego etapu jest obrócenie żółtych narożników tak, aby cała żółta ściana znalazła się u góry. Żółtą ścianę trzymamy na górze kostki.""",
        ),
        image("orientacja_naroznikow_1.gif"),
        ft.Text(
            """Szukamy układu, w którym jeden narożnik ma żółte pole skierowane do góry, a żółte pola pozostałych trzech narożników są na bokach. Ustawiamy ten narożnik w miejscu oznaczonym na rysunku i dobieramy algorytm do kierunku obrotu pozostałych narożników.""",
        ),
        image("orientacja_naroznikow_2.gif"),
        ft.Text(
            "Tego algorytmu użyj, gdy pozostałe narożniki mają obracać się w prawo, zgodnie z ruchem wskazówek zegara.",
        ),
        image("orientacja_naroznikow_3.gif"),
        ft.Text(
            "Tego algorytmu użyj, gdy pozostałe narożniki mają obracać się w lewo, przeciwnie do ruchu wskazówek zegara.",
        ),
        ft.Text(
            """Jeśli nie widzisz układu z jednym poprawnie zorientowanym narożnikiem, wykonaj algorytm, a następnie ponownie sprawdź położenie żółtych pól. Powtarzaj, dobierając algorytm do aktualnego układu.

Uwaga: algorytm może też przestawić żółte krawędzie względem środków bocznych ścian. Ich ustawienie poprawimy w ostatnim etapie.""",
        ),
        ft.Text("Przypadki etapu 7", size=24, weight=ft.FontWeight.BOLD),
        ft.Text(
            "Poniższe przykłady pokazują, jak rozpoznać układ narożników i ustawić kostkę przed wykonaniem algorytmu w prawo.",
        ),
        image("ustawienie_ok.gif"),
        ft.Text(
            "W przypadku OK jeden narożnik jest już poprawnie zorientowany, a trzy pozostałe nie. Wykonaj odpowiedni algorytm, aby zakończyć etap.",
        ),
        ft.Row(
            controls=[
                ft.Container(
                    width=168,
                    content=ft.Column(
                        controls=[
                            image(f"ustawienie_{name}.gif"),
                            ft.Text(label, weight=ft.FontWeight.BOLD),
                            ft.Text(description),
                        ],
                        spacing=4,
                    ),
                )
                for name, label, description in cases
            ],
            wrap=True,
            spacing=8,
            run_spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
        ft.Text(
            "Po poprawnym ustawieniu kostki do orientacji narożników wystarczą najwyżej dwa powtórzenia algorytmu. Po zakończeniu przejdź do ostatniego etapu.",
        ),
    ]
    if on_next is not None:
        controls.append(
            ft.Button(
                content="Etap 8 - ostatnia permutacja",
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
