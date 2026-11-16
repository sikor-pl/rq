import flet as ft


def illustration(number: int) -> ft.Image:
    filename = f"ii_warstwa_{number}.gif"
    return ft.Image(
        src=filename,
        fit=ft.BoxFit.CONTAIN,
        error_content=ft.Text(f"Dodaj do assets: {filename}"),
    )


def build_page() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Etap 3 - druga warstwa", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Przechodzimy do kolejnego etapu, czyli układanie drugiej warstwy kostki. Poniższy obrazek pokazuje co mamy uzyskać:"),
            illustration(1),
            ft.Text("""Układając II warstwę wyjątkowo będziemy trzymać naszą, już ułożoną białą ścianę, po lewej stronie, aby mieć lepszy widok na klocki, które należy wrzucić do II warstwy.

Zaczynamy od wyszukania klocka, który leży na dolnej warstwie (u nas jest to ścianka prawa, ponieważ przekręciliśmy kostkę). Następnie należy ustawić go w pozycji jak na jednym z poniższych rysunków, i wykonując jeden z poniższych algorytmów umieścić klocek na właściwym miejscu.""" 
            ),
            illustration(2),
            ft.Text("""Wyszukując klocka do włożenia na środkową warstwę na prawej ścianie należy szukać klocków, które nie mają żółtego koloru, bo tylko takie klocki należą do II warstwy.

Podczas układania tej warstwy bardzo często zdarzy ci się przypadek, że klocek będzie już na swoim miejscu, ale niewłaściwie obrócony. Obrazuje to pierwszy z rysunków poniżej:"""),
            illustration(3),
            ft.Text("""W takim przypadku musimy postępować zgodnie z powyższym schematem, czyli:
1. Najpierw wrzucić jakikolwiek klocek (na rysunku przedstawiony jaśniejszym szarym) w miejsce źle włożonego klocka.
2. Następnie prawą ścianę przekręcić o 180 stopi.
3. I zastosować pierwszy z algorytmów do włożenia klocka na swoje miejsce już w prawidłowej orientacji.

Może ci się też zdarzyć sytuacja, że po włożeniu dwóch klocków zostaną 2, ale zamienione sobą miejscami:"""),
            illustration(4),
            ft.Text("""W tym przypadku postępujemy analogicznie jak w powyższym przypadku - najpierw wyrzucamy jeden z klocków do prawej warstwy, wstawiamy go na miejsce i wstawiamy na miejsce ostatni klocek.

To już koniec etapu 3 - możesz przejść do kolejnego"""),
            # ft.Text("Statystyki drugiej warstwy", size=24, weight=ft.FontWeight.BOLD),
            # ft.Text("Miejsce na opis statystyk."),
            # ft.Row(
            #     scroll=ft.ScrollMode.AUTO,
            #     controls=[
            #         ft.DataTable(
            #             columns=[
            #                 ft.DataColumn(label=ft.Text("Powtórzenia")),
            #                 ft.DataColumn(label=ft.Text("Wystąpienia")),
            #                 ft.DataColumn(label=ft.Text("Procent")),
            #             ],
            #             rows=[
            #                 ft.DataRow(
            #                     cells=[
            #                         ft.DataCell(ft.Text(f"{number}")),
            #                         ft.DataCell(ft.Text("—")),
            #                         ft.DataCell(ft.Text("—")),
            #                     ]
            #                 )
            #                 for number in range(2, 7)
            #             ],
            #         ),
            #     ],
            # ),
            # ft.Text("Miejsce na wnioski ze statystyk."),
            ft.Text("Metoda alternatywna", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("W układaniu II warstwy istnieje metoda alternatywna nazwana \"working corner\". Polega ona na pozostawieniu jednego wolnego narożnika białej ściany po to, aby wkładanie odpowiednich klocków do II warstwy wymagało tylko 3 ruchów zamiast 8."),
            illustration(5),
            ft.Text("Na środkowej i dolnej warstwie szukamy sytuacji do przemieszczenia klocka jak na rysunku powyżej, a w miejscu zaznaczonym jaśniejszym szarym ustawiamy nasze puste miejsce. Na powyższym rysunku celowo nie zaznaczono kolorów bocznych białej ściany, gdyż jest to nieistotnie. Białą górną ścianą kręcimy tak, aby zawsze pusty narożnik znalazł się nad miejscem do włożenia klocka na drugą warstwę - poniżej przykładowa sytuacja:"),
            illustration(6),
            ft.Text("Po wrzuceniu 3 klocków drugiej warstwy wstawiamy na miejsce ostatni biały narożnik (1) jak na rysunku poniżej, po czym czwarty z klocków drugiej warstwy (2) wkładamy już metodą klasyczną wymagającą 8 ruchów."),
            illustration(7),
            ft.Text("""Prześledźmy zyski z tej metody dla standardowego przypadku, czyli włożenie 4 klocków II warstwy:
metoda klasyczna: 8 ruchów + 8 ruchów + 8 ruchów + 8 ruchów = 32 ruchy
metoda working corner: 3 ruchy + 3 ruchy + 3 ruchy + 8 ruchów = 17 ruchów
Wykonujemy zatem połowę mniej ruchów niż przy metodzie klasycznej. Mnie jednak ta metoda nie przekonała i pomimo większej ilości ruchów układam metodą klasyczną, ale wybór należy do Ciebie...

Kolejny etap"""),
        ],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
