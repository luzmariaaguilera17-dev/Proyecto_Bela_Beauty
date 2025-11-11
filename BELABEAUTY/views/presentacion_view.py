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
                ft.Row([
                    ft.Image(src="assets/marlene.jpg", width=320, height=320, fit=ft.ImageFit.COVER),
                    ft.Column([
                        ft.Text("Manicurista", italic=True),
                        ft.Text("Marlene Aguilera", size=32, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "Las uñas perfectas reflejan una actitud positiva y poderosa. "
                            "Te ayudo a sacar tu mejor versión comenzando por tus uñas.",
                            size=14, color=ft.Colors.BLACK54, width=420
                        ),
                        ft.ElevatedButton("Iniciar →", on_click=go_next, bgcolor=ft.Colors.AMBER_200)
                    ], spacing=10)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ])
        ]
