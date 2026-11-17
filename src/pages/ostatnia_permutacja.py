import flet as ft


def build_page() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text(
                "Etap 8 — ostatnia permutacja",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text(
                """Dotarłeś do ostatniego etapu układania kostki. Teraz tylko drobna kosmetyka i kostka gotowa.
Co mamy uzyskać stosując ostatnią permutację:""",
            ),
            ft.Image(
                src="ostatnia_permutacja_1.gif",
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Text(
                """Poniżej dwa algorytmy zmieniające miejsca klocków krawędziowych. Pierwszy z nich przestawia klocki zgodnie ze wskazówkami zegara. Ustawiamy kostkę żółtą ścianą do góry i wykonujemy poniższy algorytm.""",
            ),
            ft.Image(
                src="ostatnia_permutacja_2.gif",
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Text("Jeśli krawędzie mają zmieniać swoje miejsca przeciwnie do wskazówek zegara wykonujemy poniższy algorytm."),
            ft.Image(
                src="ostatnia_permutacja_3.gif",
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Text(
                "Powyższy algorytm jest identyczny jak ten w etapie 5",
            ),
            ft.Text(
                "Jeżeli przy tym etapie okaże się, że nie 3, a wszystkie 4 krawędzie są na niewłaściwych miejscach, musisz wykonać ten algorytm dwukrotnie.",
            ),
            ft.Text("TO JUŻ KONIEC UKŁADANIA! GRATULACJE!!!!!!"),
        ],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
