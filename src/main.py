import flet as ft

from circles_theme import theme, dark_theme

from pages.home_page import HomePage
from pages.circle_explore_page import CircleExplorePage
from pages.my_circles import MyCirclesPage
from pages.messages_page import MessagesPage
from pages.settings_page import SettingsPage

from login_view import LoginView

def main(page: ft.Page):
    page.title = "Circles"
    page.theme = theme
    page.dark_theme = dark_theme
    page.theme_mode = ft.ThemeMode.LIGHT

    def on_login(e):
        page.session.set("username", page.auth.user["name"])
        page.session.set("email", page.auth.user["email"])
        page.session.set("access_token", page.auth.token.access_token)
        page.session.set("img_url", page.auth.user["picture"])

        page.appbar.actions[0].content.foreground_image_src = page.session.get('img_url')
        user_dialog.content.content.controls[0].foreground_image_src = page.session.get('img_url')
        user_dialog.content.content.controls[1].value = page.session.get('username')

        page.go("/")

    def on_logout(e):
        page.go("/login")

    page.on_login = on_login
    page.on_logout = on_logout

    def on_route_change(e):
        page.views.clear()
        match page.route:
            case "/":
                if not page.auth:
                    page.go("/login")

                else:
                    page.views.append(
                        ft.View(
                            route="/",
                            appbar=page.appbar,
                            controls=page.controls
                        )
                    )

            case "/login":
                if page.auth:
                    page.go("/")
                else:
                    page.views.append(
                        LoginView(page)
                    )

        page.update()

    def on_view_pop(route):
        page.views.pop()

        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = on_route_change
    page.on_view_pop = on_view_pop

    sidebar_ref = ft.Ref[ft.Container]()
    content_ref = ft.Ref[ft.Container]()

    page.appbar = ft.AppBar(
        force_material_transparency=True,
        leading=ft.Container(
            padding=5,
            content=ft.Image(
                src="images/logo.svg"
            )
        ),
        title=ft.Text(
            value="Circles."
        ),
        actions=[
            ft.IconButton(
                content=ft.CircleAvatar(),
                style=ft.ButtonStyle(
                    padding=4
                ),
                on_click=lambda _: page.open(user_dialog)
            )
        ]
    )

    pages = {
        "Home": HomePage(page),
        "Explore Circles": CircleExplorePage(page),
        "My Circles": MyCirclesPage(page),
        "Messages": MessagesPage(page),
        "Settings": SettingsPage(page),
    }

    def open_active_page(title):
        content_ref.current.content = pages[title]

        page.update()
    
    class NavItem(ft.Container):
        def __init__(self, title, icon, active=False):
            self.active = active
            self.data = {"is_selected": False if not self.active else True}
            super().__init__(self, data=self.data)
            self.title = title
            self.icon = icon
        
        def build(self):
            self.padding = ft.padding.only(left=10, top=15, bottom=15)
            self.border_radius = 12
            self.bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST if self.data["is_selected"] else ft.Colors.TRANSPARENT
            self.content=ft.Row([
                ft.Image(
                    src=f"icons/{self.icon}.svg",
                    color=ft.Colors.PRIMARY if self.data["is_selected"] else ft.Colors.ON_SURFACE,
                ),
                ft.Text(
                    value=self.title,
                    size=18,
                    weight=ft.FontWeight.W_700,
                    color=ft.Colors.PRIMARY if self.data["is_selected"] else ft.Colors.ON_SURFACE
                )
            ])

            self.on_click = self.on_change

        def on_change(self, e):
            for i in nav_links.controls:
                i.data["is_selected"] = False
                i.build()

            self.data["is_selected"] = True
            self.build()
            page.update()
            open_active_page(self.title)


    nav_links = ft.Column([
        NavItem("Home", "home", True),
        NavItem("Explore Circles", "explore"),
        NavItem("My Circles", "group"),
        NavItem("Messages", "chat"),
        NavItem("Settings", "settings"),
    ], spacing=5)

    rail = ft.NavigationRail(
        expand=True,
        bgcolor=ft.Colors.TRANSPARENT,
        leading=ft.Container(
            ref=sidebar_ref,
            content=nav_links
        )
    )

    user_dialog = ft.AlertDialog(
        shape=ft.RoundedRectangleBorder(12),
        title=ft.Text(
            value="Profile"
        ),
        content=ft.Container(
            width=300,
            alignment=ft.alignment.top_center,
            content=ft.Column([
                ft.CircleAvatar(
                    radius=100,
                ),
                ft.TextField(
                    label="Username",
                    value="Navis Ayara"
                ),
                ft.ElevatedButton(
                    icon=ft.Icons.LOGOUT_OUTLINED,
                    text="Logout",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(12),
                        padding=10
                    ),
                    on_click=lambda _: page.logout()
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
    )

    page.overlay.append(user_dialog)

    page.add(
        ft.Row([
            ft.Container(
                width=320,
                content=rail
            ),
            ft.Container(
                expand=True,
                ref=content_ref
            )
        ], expand=True)
    )

    open_active_page("Settings")

    page.go(page.route)


ft.app(target=main, port=8550)
