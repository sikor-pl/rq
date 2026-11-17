import os
from pathlib import Path

import flet as ft

from pages import (
    bialy_krzyz,
    druga_warstwa,
    home_page,
    informacje_wstepne,
    narozniki_bialej_sciany,
    ostatnia_permutacja,
    permutacja_naroznikow,
    permutacja_zoltego_krzyza,
    orientacja_naroznikow,
    settings_page,
    zolty_krzyz,
)


def main(page: ft.Page):
    page.title = "Nawigacja Flet"

    pdf_filename = "3x3x3_algorytmy_druk.pdf"
    if page.web:
        pdf_url = pdf_filename
    else:
        assets_dir = Path(os.environ.get("FLET_ASSETS_DIR", Path(__file__).parent / "assets"))
        pdf_url = (assets_dir / pdf_filename).resolve().as_uri()

    page_builders = (
        home_page.build_page,
        lambda: informacje_wstepne.build_page(lambda: navigate_to(3)),
        settings_page.build_page,
        lambda: bialy_krzyz.build_page(lambda: navigate_to(4)),
        lambda: narozniki_bialej_sciany.build_page(lambda: navigate_to(5)),
        lambda: druga_warstwa.build_page(lambda: navigate_to(6)),
        lambda: zolty_krzyz.build_page(lambda: navigate_to(7)),
        lambda: permutacja_zoltego_krzyza.build_page(lambda: navigate_to(8)),
        lambda: permutacja_naroznikow.build_page(lambda: navigate_to(9)),
        lambda: orientacja_naroznikow.build_page(lambda: navigate_to(10)),
        ostatnia_permutacja.build_page,
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
                leading=ft.Icons.FILTER_1_OUTLINED,
                dense=True,
                on_click=click_handler(3),
            ),
            ft.ListTile(
                key=f"nav-white-corners{suffix}",
                title="Etap 2 - narożniki białej ściany",
                leading=ft.Icons.FILTER_2_OUTLINED,
                dense=True,
                on_click=click_handler(4),
            ),
            ft.ListTile(
                key=f"nav-second-layer{suffix}",
                
                title="Etap 3 - druga warstwa",
                leading=ft.Icons.FILTER_3_OUTLINED,
                dense=True,
                on_click=click_handler(5),
            ),
            ft.ListTile(
                key=f"nav-yellow-cross{suffix}",
                title="Etap 4 - żółty krzyż",
                leading=ft.Icons.FILTER_4_OUTLINED,
                dense=True,
                on_click=click_handler(6),
            ),
            ft.ListTile(
                key=f"nav-yellow-cross-permutation{suffix}",
                title="Etap 5 - permutacja żółtego krzyża",
                leading=ft.Icons.FILTER_5_OUTLINED,
                dense=True,
                on_click=click_handler(7),
            ),
            ft.ListTile(
                key=f"nav-corner-permutation{suffix}",
                title="Etap 6 - permutacja narożników",
                leading=ft.Icons.FILTER_6_OUTLINED,
                dense=True,
                on_click=click_handler(8),
            ),
            ft.ListTile(
                key=f"nav-corner-orientation{suffix}",
                title="Etap 7 - orientacja narożników",
                leading=ft.Icons.FILTER_7_OUTLINED,
                dense=True,
                on_click=click_handler(9),
            ),
            ft.ListTile(
                key=f"nav-last-permutation{suffix}",
                title="Etap 8 - ostatnia permutacja",
                leading=ft.Icons.FILTER_8_OUTLINED,
                dense=True,
                on_click=click_handler(10),
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
                controls=[
                    items[1],
                    items[3],
                    items[4],
                    items[5],
                    items[6],
                    items[7],
                    items[8],
                    items[9],
                    items[10],
                    ft.ListTile(
                        key=f"nav-print-version{suffix}",
                        title="Wersja do druku",
                        leading=ft.Icons.PRINT_OUTLINED,
                        dense=True,
                        url=ft.Url(pdf_url, target=ft.UrlTarget.BLANK),
                        on_click=lambda e: close_menu(e),
                    ),
                ],
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
