from collections.abc import Callable

import flet as ft


def build_page(on_next: Callable[[], None]) -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text(
                "Etap 2 - narożniki białej ściany",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text("""Na tym etapie układania kostki należy powkładać 4 narożniki zawierające biały kolor w odpowiednie rogi, aby utworzyły całą białą ściankę oraz pierwszą warstwę kostki.
Poniższy obrazek pokazuje, co należy uzyskać:"""),
            ft.Image(
                src="narozniki_bialej_sciany_1.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text(
                    "Dodaj do assets: narozniki_bialej_sciany_1.gif"
                ),
            ),
            ft.Text("Podobnie jak w etapie pierwszym, nie powinieneś mieć problemu z wrzuceniem białych narożników na odpowiednie miejsca. Zdaję sobie jednak sprawę, że co poniektórzy mogą mieć małe problemy, dlatego poniżej kilka algorytmów. Czerwona kropka oznacza miejsce, na którym znaleźć ma się biała ścianka narożnego klocka:"),
            ft.Image(
                src="narozniki_bialej_sciany_2.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text(
                    "Dodaj do assets: narozniki_bialej_sciany_2.gif"
                ),
            ),
            ft.Text("""Zdarzyć się też może przypadek, że klocek narożny z białym polem jest już na swoim miejscu, jednak jest źle obrócony. W takim przypadku należy go najpierw przerzucić do dolnej ściany, a następnie zastosować jeden z powyższych algorytmów wrzucając go na miejsce już w dobrej orientacji.
Poniżej dwa przypadki, kiedy musimy przerzucić niewłaściwie obrócony klocek z górnej go dolnej warstwy:
"""),
            ft.Image(
                src="narozniki_bialej_sciany_3.gif",
                fit=ft.BoxFit.CONTAIN,
                error_content=ft.Text(
                    "Dodaj do assets: narozniki_bialej_sciany_3.gif"
                ),
            ),
            ft.Text("Po zakończeniu tego etapu przechodzimy do kolejnego."),
            ft.Button(
                content="Etap 3 - druga warstwa",
                icon=ft.Icons.ARROW_FORWARD,
                on_click=on_next,
            ),
        ],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
