import flet as ft
from views.navbar import NavBar

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        def go_next(e):
            self.page.go("/presentacion")

        self.controls = [
            ft.Column([
                NavBar(self.page),
                ft.Row([
                    ft.Column([
                        ft.Container(
                            ft.Image(src="assets/home.jpg", fit=ft.ImageFit.CONTAIN),
                            width=400, height=300, border_radius=12,
                            bgcolor=ft.Colors.AMBER_50, alignment=ft.alignment.center
                        ),
                        ft.ElevatedButton("Iniciar →", on_click=go_next, bgcolor=ft.Colors.AMBER_200)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Column([
                        ft.Text("Bela Beauty Salon", size=42, weight=ft.FontWeight.BOLD),
                        ft.Container(
                            ft.Text("FOTOS", weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.AMBER_100, padding=ft.padding.all(20),
                            border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
            ])
        ]
