import flet.testing as ftt


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
