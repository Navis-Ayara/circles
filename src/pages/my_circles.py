import flet as ft


class MyCirclesPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.circle_name = ft.Ref[ft.TextField]()
        self.circle_description = ft.Ref[ft.TextField]()
        self.circle_image = ft.Ref[ft.IconButton]()

        self.my_circles = []

    def build(self):
        self.spacing = 0
        self.circle_create_form = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create a Circle"),
            content=ft.Container(
                width=600,
                height=320,
                padding=10,
                content=ft.Column([
                    ft.TextField(
                        label="Name",
                        max_length=14,
                        ref=self.circle_name
                    ),
                    ft.TextField(
                        label="Description",
                        max_length=14,
                        ref=self.circle_description,
                    ),
                    ft.IconButton(
                        width=170,
                        height=170,
                        content=ft.Stack([
                            ft.CircleAvatar(
                                radius=140
                            ),
                            ft.Icon(ft.Icons.PHOTO_CAMERA_OUTLINED, size=32)
                        ], alignment=ft.alignment.center),
                        ref=self.circle_image,
                    ),
                    ft.Text("Add a photo")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ),
            actions=[
                ft.TextButton(
                    text="Cancel",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(12),
                        color=ft.Colors.RED_ACCENT,
                        overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.RED),
                    ),
                    on_click=self.close_dlg
                ),
                ft.ElevatedButton(
                    text="Create",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(12)
                    ),
                    on_click=self.create_circle
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        self.page.overlay.append(self.circle_create_form)
        self.controls = [
            ft.Row([
                ft.OutlinedButton(
                    text="Create new Circle",
                    on_click=self.open_dlg
                )
            ], alignment=ft.MainAxisAlignment.END),
            ft.Row(
                spacing=0,
                expand=True,
                controls=[
                    ft.Container(
                        width=300,
                        border=ft.border.only(
                            left=ft.BorderSide(1.2, ft.Colors.ON_SECONDARY),
                            right=ft.BorderSide(1.2, ft.Colors.ON_SECONDARY)
                        ),
                        content=ft.ListView([
                            ft.Card(
                                elevation=5,
                                content=ft.Container(
                                    border_radius=12,
                                    content=ft.ListTile(
                                        height=55,
                                        leading=ft.CircleAvatar(),
                                        title=ft.Text(
                                            value=i["name"]
                                        ),
                                        shape=ft.RoundedRectangleBorder(12),
                                        on_click=lambda _: print("Navis you mad dawg")
                                    ),
                                )
                            )
                        for i in self.page.session.get("my_circles")], spacing=10, padding=ft.padding.only(left=10, right=10), expand=True)
                    ),
                    ft.ListView([
                        
                    ], spacing=10, padding=ft.padding.only(left=100, right=100), expand=True),
                ]
            ) if self.page.session.get("my_circles") is not None else (
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value="No Circles yet\nCreate or join a new one!",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            )
        ]

    def open_dlg(self, e):
        self.circle_create_form.open = True

        self.circle_create_form.update()

    def close_dlg(self, e):
        self.circle_create_form.open = False

        self.circle_create_form.update()

    def create_circle(self, e):
        self.my_circles.append(
            {
                "id": len(self.my_circles)+1,
                "name": self.circle_name.current.value,
                "description": self.circle_description.current.value,
                "image_url": self.circle_image.current.content.controls[0].foreground_image_src
            }
        )
        self.circle_name.current.value = ""
        self.circle_description.current.value =""
        self.circle_image.current.content = ft.Stack([
            ft.CircleAvatar(
                radius=140
            ),
            ft.Icon(ft.Icons.PHOTO_CAMERA_OUTLINED, size=32)
        ], alignment=ft.alignment.center)

        self.page.session.set("my_circles", self.my_circles)
        self.circle_create_form.open = False

        self.circle_create_form.update()
        self.build()
        self.page.update()

