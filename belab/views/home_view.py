import flet as ft

def HomeView(navegar):
    return ft.Column(
        [
            ft.Text("Bienvenida a Bela Beauty Salon", size=28, weight="bold", color="black"),
            ft.Text("Por favor inicia sesión para continuar", size=18, color="gray"),
            ft.TextField(label="Usuario", width=300),
            ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300),
            ft.ElevatedButton("Iniciar Sesión", bgcolor="black", color="white", on_click=lambda e: navegar("servicios")),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    )
