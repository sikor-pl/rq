import flet as ft

from pages import (
    bialy_krzyz,
    druga_warstwa,
    home_page,
    informacje_wstepne,
    narozniki_bialej_sciany,
    settings_page,
)


def main(page: ft.Page):
    page.title = "Nawigacja Flet"

    page_builders = (
        home_page.build_page,
        lambda: informacje_wstepne.build_page(lambda: navigate_to(3)),
        settings_page.build_page,
        lambda: bialy_krzyz.build_page(lambda: navigate_to(4)),
        lambda: narozniki_bialej_sciany.build_page(lambda: navigate_to(5)),
        druga_warstwa.build_page,
    )
    page_content = ft.Container(
        content=page_builders[0](),
        expand=True,
        padding=24,
    )

    def navigate_to(index: int) -> None:
        page_content.content = page_builders[index]()
        for items in (desktop_items, mobile_items):
            for item_index, item in enumerate(items):
                item.selected = item_index == index
        mobile_overlay.visible = False
        page.update()

    def create_menu(mobile: bool) -> tuple[list[ft.Control], list[ft.ListTile]]:
        suffix = "-mobile" if mobile else ""

        def click_handler(index: int):
            def handle_click(e: ft.Event[ft.ListTile]) -> None:
                navigate_to(index)

            return handle_click

        items = [
            ft.ListTile(
                key=f"nav-home{suffix}",
                title="Strona główna",
                leading=ft.Icons.HOME_OUTLINED,
                selected=True,
                on_click=click_handler(0),
            ),
            ft.ListTile(
                key=f"nav-cube-information{suffix}",
                title="Informacje wstępne",
                leading=ft.Icons.INFO_OUTLINE,
                dense=True,
                on_click=click_handler(1),
            ),
            ft.ListTile(
                key=f"nav-settings{suffix}",
                title="Ustawienia",
                leading=ft.Icons.SETTINGS_OUTLINED,
                on_click=click_handler(2),
            ),
            ft.ListTile(
                key=f"nav-white-cross{suffix}",
                title="Etap 1 - biały krzyż",
                leading=ft.Icons.LOOKS_ONE_OUTLINED,
                dense=True,
                on_click=click_handler(3),
            ),
            ft.ListTile(
                key=f"nav-white-corners{suffix}",
                title="Etap 2 - narożniki białej ściany",
                leading=ft.Icons.LOOKS_TWO_OUTLINED,
                dense=True,
                on_click=click_handler(4),
            ),
            ft.ListTile(
                key=f"nav-second-layer{suffix}",
                
                title="Etap 3 - druga warstwa",
                leading=ft.Icons.LOOKS_3_OUTLINED,
                dense=True,
                on_click=click_handler(5),
            ),
        ]
        return [
            ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            items[0],
            ft.ExpansionTile(
                key=f"nav-cube{suffix}",
                title="Kostka 3x3",
                leading=ft.Icons.LOOKS_3,
                controls=[items[1], items[3], items[4], items[5]],
            ),
            items[2],
        ], items

    desktop_controls, desktop_items = create_menu(mobile=False)
    mobile_controls, mobile_items = create_menu(mobile=True)

    sidebar = ft.Container(
        width=260,
        padding=8,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        content=ft.Column(
            controls=desktop_controls,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
    )
    divider = ft.VerticalDivider(width=1)

    def close_menu(e: ft.Event) -> None:
        mobile_overlay.visible = False
        page.update()

    mobile_panel = ft.Container(
        left=0,
        top=0,
        bottom=0,
        width=260,
        padding=8,
        bgcolor=ft.Colors.SURFACE_CONTAINER,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD, expand=True),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            tooltip="Zamknij menu",
                            on_click=close_menu,
                        ),
                    ],
                ),
                *mobile_controls[1:],
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
    )
    mobile_overlay = ft.Stack(
        controls=[
            ft.Container(
                left=0,
                top=0,
                right=0,
                bottom=0,
                bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
                on_click=close_menu,
            ),
            mobile_panel,
        ],
        left=0,
        top=0,
        right=0,
        bottom=0,
        visible=False,
    )

    def open_menu(e: ft.Event[ft.IconButton]) -> None:
        mobile_overlay.visible = True
        page.update()

    mobile_header = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.MENU,
                tooltip="Otwórz menu",
                on_click=open_menu,
            ),
            ft.Text("Menu", size=20, weight=ft.FontWeight.BOLD),
        ],
    )

    def set_layout(width: float | None) -> None:
        compact = width is None or width < 600
        sidebar.visible = not compact
        divider.visible = not compact
        mobile_header.visible = compact
        page_content.padding = 16 if compact else 24
        if width is not None:
            mobile_panel.width = min(260, width)
        if not compact:
            mobile_overlay.visible = False

    def on_resize(e: ft.PageResizeEvent) -> None:
        set_layout(e.width)
        page.update()

    set_layout(page.width)
    page.on_resize = on_resize

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            mobile_header,
                            ft.Row(
                                controls=[sidebar, divider, page_content],
                                expand=True,
                                spacing=0,
                            ),
                        ],
                        expand=True,
                        spacing=0,
                    ),
                    mobile_overlay,
                ],
                expand=True,
                fit=ft.StackFit.EXPAND,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
