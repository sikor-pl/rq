from unittest.mock import Mock

import flet as ft
import flet.testing as ftt

from main import main
from pages import permutacja_naroznikow, permutacja_zoltego_krzyza


async def test_expandable_menu_navigation(flet_app: ftt.FletTestApp):
    tester = flet_app.tester

    await tester.pump_and_settle()
    assert (await tester.find_by_text(" Jak układać kostkę Rubika")).count == 1

    await tester.tap(await tester.find_by_key("nav-cube"))
    await tester.pump_and_settle()
    await tester.tap(await tester.find_by_key("nav-cube-information"))
    await tester.pump_and_settle()
    assert (await tester.find_by_text("Informacje wstępne")).count == 1

    await tester.tap(await tester.find_by_key("nav-settings"))
    await tester.pump_and_settle()
    assert (await tester.find_by_text("Preferencje aplikacji")).count == 1

    await tester.tap(await tester.find_by_key("nav-home"))
    await tester.pump_and_settle()
    assert (await tester.find_by_text(" Jak układać kostkę Rubika")).count == 1


def test_yellow_cross_navigation():
    page = Mock(spec=ft.Page)
    page.width = 1000
    main(page)

    root = page.add.call_args.args[0]
    stack = root.content
    layout = stack.controls[0]
    sidebar, _, content = layout.controls[1].controls
    desktop_menu = sidebar.content.controls[3]
    mobile_overlay = stack.controls[1]
    mobile_panel = mobile_overlay.controls[1]
    mobile_menu = mobile_panel.content.controls[3]

    def find_item(menu, key):
        return next(item for item in menu.controls if item.key.split("-mobile")[0] == key)

    for menu in (desktop_menu, mobile_menu):
        yellow_cross = find_item(menu, "nav-yellow-cross")
        assert yellow_cross.key.startswith("nav-yellow-cross")
        yellow_cross.on_click(None)
        assert content.content.controls[0].value == "Etap 4 - żółty krzyż"

    find_item(desktop_menu, "nav-second-layer").on_click(None)
    next_button = content.content.controls[-1]
    assert next_button.content == "Etap 4 - żółty krzyż"
    next_button.on_click()
    assert content.content.controls[0].value == "Etap 4 - żółty krzyż"
    assert [
        control.src for control in content.content.controls
        if isinstance(control, ft.Image)
    ] == ["zolty_krzyz_3.gif", "zolty_krzyz_1.gif", "zolty_krzyz_2.gif"]

    next_button = content.content.controls[-1]
    next_button.on_click()
    assert content.content.controls[0].value == "Etap 5 - permutacja żółtego krzyża"
    assert not any(
        "statystyk" in control.value.lower()
        for control in content.content.controls
        if isinstance(control, ft.Text)
    )

    next_button = content.content.controls[-1]
    assert next_button.content == "Etap 6 - permutacja narożników"
    next_button.on_click()
    assert content.content.controls[0].value == "Etap 6 — permutacja narożników"

    for menu in (desktop_menu, mobile_menu):
        permutation = find_item(menu, "nav-yellow-cross-permutation")
        assert permutation.key.startswith("nav-yellow-cross-permutation")
        permutation.on_click(None)
        assert content.content.controls[0].value == "Etap 5 - permutacja żółtego krzyża"
        find_item(menu, "nav-corner-permutation").on_click(None)
        assert content.content.controls[0].value == "Etap 6 — permutacja narożników"


def test_permutation_cases_show_descriptions_under_images():
    page = permutacja_zoltego_krzyza.build_page()
    row = next(control for control in page.controls if isinstance(control, ft.Row))

    assert row.wrap
    assert len(row.controls) == 3
    for number, case in zip((21, 22, 23), row.controls):
        image, description = case.content.controls
        assert image.src == f"permutacja_zoltego_krzyza_{number}.gif"
        assert isinstance(description, ft.Text)
        assert description.value
    algorithm = page.controls[page.controls.index(row) + 1]
    assert isinstance(algorithm, ft.Image)
    assert algorithm.src == "permutacja_zoltego_krzyza_a.gif"


def test_corner_permutation_page_has_empty_copy_and_image_slots_without_statistics():
    page = permutacja_naroznikow.build_page()
    slots = {
        control.key: control
        for control in page.controls
        if isinstance(control, ft.Container) and control.key
    }

    assert "corner-permutation-introduction" in slots
    assert "corner-permutation-position-example" in slots
    assert "corner-permutation-right-algorithm" in slots
    assert "corner-permutation-left-algorithm" in slots
    assert all(
        control.content.value == "Miejsce na opis"
        for key, control in slots.items()
        if key.endswith("description")
    )
    assert not any(
        "statystyk" in control.value.lower()
        for control in page.controls
        if isinstance(control, ft.Text)
    )
