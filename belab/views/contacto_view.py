import flet as ft

def ContactoView():
    return ft.Column(
        [
            ft.Text("Contáctanos", size=28, weight="bold", color="#ff8c42"),
            ft.Text("Dirección: Av. Belleza #123, Ciudad"),
            ft.Text("Teléfono: +54 9 1123 4567"),
            ft.Text("Email: contacto@belabeauty.com"),
            ft.TextField(label="Tu nombre", width=300, border_color="#ff8c42"),
            ft.TextField(label="Tu mensaje", width=300, multiline=True, border_color="#ff8c42"),
            ft.ElevatedButton("Enviar", bgcolor="#ff8c42", color="white", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
