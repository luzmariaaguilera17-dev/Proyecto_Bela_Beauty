import flet as ft
from views.navbar import NavBar

class ServiciosView(ft.View):
    def _init_(self, page: ft.Page):
        super()._init_("/servicios", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        servicios = [
            ("Manicura simple", "15 USD", "45 min"),
            ("Acrílico completo", "40 USD", "90 min"),
            ("Esmaltado semipermanente", "25 USD", "60 min"),
            ("Decoración / Nail art", "10-20 USD", "30-45 min"),
        ]

        lista = ft.Column(
            [
                ft.Row(
                    [ft.Text(s, size=16), ft.Text(p), ft.Text(t)],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                for s, p, t in servicios
            ],
            spacing=8
        )

        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        NavBar(self.page),
                        ft.Text("Servicios", size=28, weight=ft.FontWeight.BOLD),
                        lista,
                        ft.Divider(),
                        ft.Text("¿Deseas reservar un servicio? Ve a la sección Horarios.", italic=True)
                    ],
                    spacing=12
                ),
                padding=20  # ✅ Padding aplicado en el Container
            )
        ]