import flet as ft

from pages import home_page, informacje_wstepne, settings_page


def main(page: ft.Page):
    page.title = "Nawigacja Flet"

    page_builders = (
        home_page.build_page,
        informacje_wstepne.build_page,
        settings_page.build_page,
    )
    page_content = ft.Container(
        content=page_builders[0](),
        expand=True,
        padding=24,
    )

    def navigate_to(index: int) -> None:
        page_content.content = page_builders[index]()
        home_item.selected = index == 0
        information_item.selected = index == 1
        settings_item.selected = index == 2
        page.update()

    home_item = ft.ListTile(
        key="nav-home",
        title="Strona główna",
        leading=ft.Icons.HOME_OUTLINED,
        selected=True,
        on_click=lambda _: navigate_to(0),
    )
    information_item = ft.ListTile(
        key="nav-cube-information",
        title="Informacje wstępne",
        leading=ft.Icons.INFO_OUTLINE,
        dense=True,
        on_click=lambda _: navigate_to(1),
    )
    settings_item = ft.ListTile(
        key="nav-settings",
        title="Ustawienia",
        leading=ft.Icons.SETTINGS_OUTLINED,
        on_click=lambda _: navigate_to(2),
    )
    cube_menu = ft.ExpansionTile(
        key="nav-cube",
        title="Kostka 3x3",
        leading=ft.Icons.LOOKS_3,
        controls=[information_item],
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=260,
                        padding=8,
                        bgcolor=ft.Colors.SURFACE_CONTAINER,
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Menu",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Divider(),
                                home_item,
                                cube_menu,
                                settings_item,
                            ],
                            spacing=0,
                            expand=True,
                        ),
                    ),
                    ft.VerticalDivider(width=1),
                    page_content,
                ],
                expand=True,
                spacing=0,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
