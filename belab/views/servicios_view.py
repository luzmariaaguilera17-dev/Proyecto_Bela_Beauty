import flet as ft

def ServiciosView():
    return ft.Column(
        [
            ft.Text("Nuestros Servicios", size=28, weight="bold"),
            ft.Text("💅 Manicure y Pedicure"),
            ft.Text("✨ Uñas acrílicas y gel"),
            ft.Text("🧖 Depilación y tratamientos faciales"),
            ft.Text("💋 Maquillaje profesional"),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
