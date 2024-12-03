import flet as ft


class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

    def build(self):
        self.content = ft.Container(
            border_radius=12,
            bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY_200),
            expand=True,
            padding=17,
            content=ft.Column([
                self.create_settings_item(
                    title="Theme",
                    controls=[
                        ft.RadioGroup(
                            on_change=self.change_theme,
                            value="system",
                            content=ft.Column([
                                ft.Radio(
                                    label="Light",
                                    value="light"
                                ),
                                ft.Radio(
                                    label="Dark",
                                    value="dark"
                                ),
                                ft.Radio(
                                    label="System",
                                    value="system"
                                )
                            ], spacing=2)
                        )
                    ]
                ),
                self.create_settings_item(
                    title="More settings coming soon",
                    controls=[
                        ft.Container()
                    ]
                )
            ])
        )

    def create_settings_item(self, title, controls: list[ft.Control]):
        return ft.Column([
            ft.Text(
                value=title,
                size=18,
                weight=ft.FontWeight.BOLD
            ),
            *controls
        ])
    
    def change_theme(self, e):
        self.page.client_storage.set("theme", e.control.value)
        self.page.theme_mode = e.control.value

        self.page.update()
