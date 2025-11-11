import flet as ft

def HomeView(navegar):
    return ft.Column(
        [
            ft.Text("Bienvenida a Bela Beauty Salon", size=30, weight="bold", color="#ff8c42"),
            ft.Text("Por favor inicia sesión para continuar", size=18, color="gray"),
            ft.TextField(label="Usuario", width=300, border_color="#ff8c42"),
            ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, border_color="#ff8c42"),
            ft.ElevatedButton(
                "Iniciar Sesión",
                bgcolor="#ff8c42",
                color="white",
                on_click=lambda e: navegar("servicios"),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    )
