import flet as ft


def build_page() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Preferencje aplikacji", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Dostosuj działanie aplikacji do swoich potrzeb."),
            ft.Switch(label="Powiadomienia", value=True),
        ],
        spacing=16,
        expand=True,
    )
