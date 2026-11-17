from pathlib import Path
from unittest.mock import Mock

import flet as ft
import pytest

from main import main


@pytest.mark.parametrize("web", [False, True])
def test_print_version_in_both_menus(web, monkeypatch):
    assets = Path(__file__).resolve().parents[1] / "src" / "assets"
    monkeypatch.setenv("FLET_ASSETS_DIR", str(assets))
    page = Mock(spec=ft.Page)
    page.web = web
    page.width = 1000
    main(page)

    stack = page.add.call_args.args[0].content
    sidebar = stack.controls[0].controls[1].controls[0]
    mobile_overlay = stack.controls[1]
    menus = (
        sidebar.content.controls[3],
        mobile_overlay.controls[1].content.controls[3],
    )
    filename = "3x3x3_algorytmy_druk.pdf"
    expected_url = filename if web else (assets / filename).as_uri()
    assert (assets / filename).is_file()

    for menu in menus:
        stage_eight, print_version = menu.controls[-2:]
        assert stage_eight.title == "Etap 8 - ostatnia permutacja"
        assert print_version.title == "Wersja do druku"
        assert print_version.url.url == expected_url
        assert print_version.url.target == ft.UrlTarget.BLANK
        mobile_overlay.visible = True
        print_version.on_click(None)
        assert not mobile_overlay.visible
