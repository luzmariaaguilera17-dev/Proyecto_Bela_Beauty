import flet as ft
import webbrowser
from views.navbar import NavBar

class UbicacionView(ft.View):
    def _init_(self, page: ft.Page):
        super()._init_("/ubicacion", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        def abrir_mapa(e):
            webbrowser.open("https://www.google.com/maps?q=Bela+Beauty+Salon")

        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        NavBar(self.page),
                        ft.Text("Ubicación", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Nos encontramos en el centro. Pulsa el botón para abrir Google Maps."),
                        ft.ElevatedButton("Abrir mapa", on_click=abrir_mapa, bgcolor=ft.Colors.AMBER_200)
                    ],
                    spacing=10
                ),
                padding=20  # ✅ Padding aplicado correctamente
            )
        ]
