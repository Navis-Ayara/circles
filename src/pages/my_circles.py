import flet as ft


class MyCirclesPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.expand = True
        self.scroll = ft.ScrollMode.ALWAYS
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def build(self):
        self.controls = [
            ft.Row([
                ft.OutlinedButton(
                    text="Create new Circle"
                )
            ], alignment=ft.MainAxisAlignment.END),
            ft.GridView([

            ]) if self.page.session.get("my_circles") is not None else (
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value="No Circles yet\nCreate a new one!",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            )
        ]
