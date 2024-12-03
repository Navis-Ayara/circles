import flet as ft


class MessagesPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.expand = True
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Image(
                    src="images/progress.svg",
                    height=300
                ),
                ft.Markdown(
                    value="# Coming soon...\nYou can contribute [here](https://github.com/Navis-Ayara/circles)",
                    auto_follow_links=True
                ),
            ]
        )
