import flet as ft


def image_placeholder(filename: str, width: int = 121, height: int = 121) -> ft.Image:
    return ft.Image(
        src=filename,
        width=width,
        height=height,
        fit=ft.BoxFit.CONTAIN,
        error_content=ft.Container(
            content=ft.Text(f"Dodaj do assets:\n{filename}", size=11),
            width=width,
            height=height,
            bgcolor=ft.Colors.SURFACE_CONTAINER,
            alignment=ft.Alignment.CENTER,
            padding=4,
        ),
    )


def build_page() -> ft.Control:
    faces = [
        ("lewa", "Lewa ściana", "LEFT (L) (w tym przypadku zielona)"),
        ("prawa", "Prawa ściana", "RIGHT (R) (w tym przypadku niebieska)"),
        ("gora", "Górna ściana", "UP (U) (w tym przypadku czerwona)"),
        ("dol", "Dolna ściana", "DOWN (D) (w tym przypadku pomarańczowa)"),
        ("przod", "Przednia ściana", "FRONT (F) (w tym przypadku żółta)"),
        ("tyl", "Tylna ściana", "BACK (B) (w tym przypadku biała)"),
    ]

    return ft.Column(
        controls=[
            ft.Text("Informacje wstępne", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("""Kostka Rubika, jako że jest sześcianem, posiada sześć ścian. Każda z nich ma inny kolor i jest inaczej nazywana.
Poniższe rysunki pokazują każdą ze ścian, jej położenie, nazwę angielską oraz kolor, który w tym przypadku reprezentuje."""),
            ft.Row(
                controls=[
                    ft.Container(
                        width=168,
                        content=ft.Column(
                            controls=[
                                image_placeholder(f"informacjeogolne_{name}.gif"),
                                ft.Text(label, weight=ft.FontWeight.BOLD),
                                ft.Text(description),
                            ],
                            spacing=4,
                        ),
                    )
                    for name, label, description in faces
                ],
                width=720,
                wrap=True,
                spacing=8,
                run_spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            ft.Text("Powyższe przykłady ukazują już poukładane ściany. Jednak jeśli kostka nie jest ułożona, kolor ściany reprezentuje jej środkowy (centralny) klocek."),
            ft.Row(
                controls=[
                    image_placeholder("informacjeogolne_rozwalona.gif"),
                    ft.Text("""W przypadku nie ułożonej kostki na rysunku obok następujące ściany są w kolorach:
                            LEWA: niebieska
                            PRAWA: zielona
                            GÓRNA: czerwona
                            DOLNA: pomarańczowa
                            PRZEDNIA: biała
                            TYLNA (tutaj niewidoczna): żółta""", expand=True),
                ],
                spacing=24,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Text("""Warto zapamiętać, że środkowe klocki kostki, czyli w rezultacie całe ściany, nie zmieniają położenia względem siebie.
Ich ułożenie zawsze jest następujące:
BIAŁA naprzeciw ŻÓŁTEJ
NIEBIESKA naprzeciw ZIELONEJ
POMARAŃCZOWA naprzeciw CZERWONEJ."""),
            image_placeholder("informacjeogolne_naprzeciw.gif", width=336, height=121),
            ft.Text("""Warto zapamiętać tą informację, ponieważ może stać się ona pomocna kiedy już będziemy układać kostkę z pamięci. Nie będziemy musieli kręcić kostką, aby dowiedzieć się jaka ściana leży po drugiej stronie.

To tyle tytułem informacji wstępnych. Możemy rozpocząć układanie kostki. Metoda przedstawiona przeze mnie w poradniku nosi nazwę LBL (Layer By Layer) czyli warstwa po warstwie. Jest to najdłuższa, bo składająca się aż z 8 etapów metoda, ale za to najłatwiejsza ze wszystkich i każdy może jej się nauczyć."""),
        ],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
