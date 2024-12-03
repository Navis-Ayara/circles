import flet as ft

class HomePage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

    def build(self):
        self.alignment = ft.alignment.center
        self.content = ft.ListView([

        ]) if self.page.session.get("posts") is not None else (
            ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src="images/empty.svg",
                        height=300
                    ),
                    ft.Text(
                        value="No posts yet\nJoin circles to populate posts or create your own",
                        text_align=ft.TextAlign.CENTER,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                ]
            )
        )
