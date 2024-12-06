import flet as ft

from utils.login import provider


class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.route = "/login"

    def build(self):
        complete_page_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Signed in to MyApp</title>
        </head>
        <body>
        <script type="text/javascript">
            window.close();
        </script>
        <p>You've been successfully signed in! You can close this tab or window now.</p>
        </body>
        </html>
        """

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value="Circles.",
                            size=36,
                            weight=ft.FontWeight.W_700
                        ),
                        ft.Image(
                            src="icon.png",
                            height=230
                        ),
                        ft.ElevatedButton(
                            text="Login with Google",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(12),
                                padding=ft.padding.only(left=20, right=20, top=6, bottom=6),
                                text_style=ft.TextStyle(
                                    size=16,
                                    weight=ft.FontWeight.W_600
                                )
                            ),
                            on_click=lambda _: self.page.login(
                                provider, 
                                fetch_user=True, 
                                on_open_authorization_url=lambda url: self.page.launch_url(url, web_window_name="_blank"),
                                complete_page_html=complete_page_html)
                        ),
                    ]
                )
            )
        ]
