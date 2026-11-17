from unittest.mock import Mock

import flet as ft

from main import main
from pages import orientacja_naroznikow


def test_corner_orientation_is_reachable_from_stage_six_and_menu():
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

    stage_six = next(
        item for item in desktop_menu.controls if item.key == "nav-corner-permutation"
    )
    stage_six.on_click(None)
    next_button = content.content.controls[-1]
    assert next_button.content == "Etap 7 - orientacja narożników"
    next_button.on_click()
    assert content.content.controls[0].value == "Etap 7 — orientacja narożników"

    for menu in (desktop_menu, mobile_menu):
        stage_seven = next(
            item
            for item in menu.controls
            if item.key == "nav-corner-orientation"
            or item.key == "nav-corner-orientation-mobile"
        )
        stage_seven.on_click(None)
        assert content.content.controls[0].value == "Etap 7 — orientacja narożników"


def test_corner_orientation_page_has_basic_cases_without_statistics_or_alternatives():
    page = orientacja_naroznikow.build_page()

    assert page.controls[0].value == "Etap 7 — orientacja narożników"
    image_sources = {
        control.src for control in page.controls if isinstance(control, ft.Image)
    }
    assert {
        "orientacja_naroznikow_1.gif",
        "orientacja_naroznikow_2.gif",
        "orientacja_naroznikow_3.gif",
        "ustawienie_ok.gif",
    }.issubset(image_sources)

    cases = next(control for control in page.controls if isinstance(control, ft.Row))
    assert cases.wrap
    assert len(cases.controls) == 5
    assert not any(
        "statystyk" in control.value.lower()
        or "alternatywn" in control.value.lower()
        for control in page.controls
        if isinstance(control, ft.Text)
    )
    assert not isinstance(page.controls[-1], ft.Button)
