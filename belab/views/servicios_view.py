import flet as ft

def ServiciosView():
    return ft.Column(
        [
            ft.Text("Nuestros Servicios", size=28, weight="bold", color="#ff8c42"),
            ft.Text("Manicure y Pedicure", size=18),
            ft.Text("Uñas acrílicas y en gel", size=18),
            ft.Text("Depilación y tratamientos faciales", size=18),
            ft.Text("Maquillaje profesional", size=18),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
