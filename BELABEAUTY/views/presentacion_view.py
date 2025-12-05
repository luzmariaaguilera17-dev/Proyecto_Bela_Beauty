import flet as ft
from views.navbar import NavBar

class PresentacionView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/presentacion", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        def go_next(e):
            self.page.go("/servicios")

        self.controls = [
            ft.Column([
                NavBar(self.page),
                ft.Container(height=20),
                ft.Row([
                    # Imagen a la izquierda con mejor diseño
                    ft.Container(
                        ft.Image(
                            src="manicurista.jpeg",
                            width=300,
                            height=300,
                            fit=ft.ImageFit.COVER,
                            border_radius=15
                        ),
                        width=320,
                        height=320,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=15,
                        padding=ft.padding.all(10),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=10,
                            color=ft.Colors.BLACK12,
                        ),
                        border=ft.border.all(2, ft.Colors.AMBER_100)
                    ),
                    ft.Container(width=50),
                    # Texto a la derecha
                    ft.Column([
                        ft.Text(
                            "MANICURISTA PROFESIONAL",
                            size=14,
                            color=ft.Colors.AMBER_600,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Text(
                            "Marlene Aguilera",
                            size=36,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.AMBER_800
                        ),
                        ft.Container(height=20),
                        ft.Text(
                            "Las uñas perfectas reflejan una actitud positiva y poderosa. "
                            "Te ayudo a sacar tu mejor versión comenzando por tus uñas.",
                            size=16,
                            color=ft.Colors.GREY_700,
                            width=400
                        ),
                        ft.Container(height=30),
                        ft.ElevatedButton(
                            "Ver servicios →",
                            on_click=go_next,
                            bgcolor=ft.Colors.AMBER_200,
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                padding=ft.padding.symmetric(horizontal=30, vertical=15)
                            ),
                            icon=ft.Icons.ARROW_FORWARD
                        )
                    ], spacing=5)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ], expand=True)
        ]