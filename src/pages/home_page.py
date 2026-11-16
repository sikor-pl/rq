import flet as ft


def build_page() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text(" Jak układać kostkę Rubika", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("""Strona ta poświęcona jest kostce Rubika, a dokładniej metodom jej układania.
Jak wiadomo, w internecie jest kilka stron poświęconych układaniu kostki. Postanowiłem je przejrzeć i wybierając najlepsze algorytmy stworzyć najwygodniejszą dla mnie metodę układania kostki.
Dodatkowo przy każdym etapie układania zobaczyć można informacje dodatkowe, ułatwienia, metody alternatywne oraz statystykę danego etapu.
W przyszłości planuję także dodanie filmików instruktażowych dotyczących każdego etapu układania.

W swoim poradniku wprowadziłem innowacyjną metodę pokazywania kostki. Dzięki zastosowaniu rozciągniętej perspektywy w moich rysunkach poglądowych widać aż 5 ścian kostki jednocześnie. W rzeczywistości taki rzut na sześcian jest niemożliwy, jednak ułatwia on układającemu zapoznanie się z aktualnym ułożeniem kolorów na kostce jednocześnie na wszystkich pięciu ścianach.
"""),
            ft.Image(
                src="assets/wstep1.gif",
                width=261,
                height=121,
                fit=ft.BoxFit.CONTAIN,
                        ),
            ft.Text("Mam nadzieję, że zamieszczony przeze mnie kurs jest jasny, nawet dla zupełnie początkujących i do prowadzi on do skutecznego ułożenia kostki Rubika.")
        ],
        spacing=16,
        expand=True,
    )
