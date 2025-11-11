import flet as ft

def NavBar(navegar):
    return ft.Container(
        bgcolor="black",
        content=ft.Row(
            controls=[
                ft.Text("💅 Bela Beauty Salon", color="white", size=22, weight="bold"),
                ft.Row(
                    controls=[
                        ft.TextButton("Inicio", on_click=lambda e: navegar("inicio"), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Servicios", on_click=lambda e: navegar("servicios"), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Contacto", on_click=lambda e: navegar("contacto"), style=ft.ButtonStyle(color="white")),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    expand=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=ft.padding.all(15),
    )

