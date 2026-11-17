from unittest.mock import Mock

import flet as ft

from main import main
from pages import ostatnia_permutacja


def test_last_permutation_page_uses_direct_images_and_omits_statistics():
    page = ostatnia_permutacja.build_page()

    assert page.controls[0].value == "Etap 8 — ostatnia permutacja"
    assert [
        control.src for control in page.controls if isinstance(control, ft.Image)
    ] == [
        "ostatnia_permutacja_1.gif",
        "ostatnia_permutacja_2.gif",
        "ostatnia_permutacja_3.gif",
    ]
    assert not any(
        "statystyk" in control.value.lower()
        for control in page.controls
        if isinstance(control, ft.Text)
    )


def test_last_permutation_is_reachable_from_stage_seven_and_menu():
    page = Mock(spec=ft.Page)
    page.width = 1000
    main(page)

    root = page.add.call_args.args[0]
    stack = root.content
    layout = stack.controls[0]
    sidebar, _, content = layout.controls[1].controls
    desktop_menu = sidebar.content.controls[3]
    mobile_panel = stack.controls[1].controls[1]
    mobile_menu = mobile_panel.content.controls[3]

    stage_seven = next(
        item for item in desktop_menu.controls if item.key == "nav-corner-orientation"
    )
    assert stage_seven.leading == ft.Icons.FILTER_7_OUTLINED
    stage_seven.on_click(None)
    next_button = content.content.controls[-1]
    assert next_button.content == "Etap 8 - ostatnia permutacja"
    next_button.on_click()
    assert content.content.controls[0].value == "Etap 8 — ostatnia permutacja"

    for menu in (desktop_menu, mobile_menu):
        stage_eight = next(
            item
            for item in menu.controls
            if item.key == "nav-last-permutation"
            or item.key == "nav-last-permutation-mobile"
        )
        assert stage_eight.leading == ft.Icons.FILTER_8_OUTLINED
        stage_eight.on_click(None)
        assert content.content.controls[0].value == "Etap 8 — ostatnia permutacja"
