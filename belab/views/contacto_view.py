import flet as ft

def ContactoView():
    return ft.Column(
        [
            ft.Text("Contáctanos", size=28, weight="bold"),
            ft.Text("📍 Dirección: Av. Belleza #123, Ciudad"),
            ft.Text("📞 Teléfono: +54 9 1123 4567"),
            ft.Text("📧 Email: contacto@belabeauty.com"),
            ft.TextField(label="Tu nombre", width=300),
            ft.TextField(label="Tu mensaje", width=300, multiline=True),
            ft.ElevatedButton("Enviar", bgcolor="black", color="white"),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
