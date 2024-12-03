import flet as ft

class CircleExplorePage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

    def build(self):
        self.content = ft.Column([
            ft.SearchBar(
                bar_shape=ft.RoundedRectangleBorder(12),
                bar_leading=ft.Icon(name=ft.Icons.SEARCH),
                bar_hint_text="Search with circle names or tags"
            ),
            ft.GridView(
                expand=True
            )
        ], expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)