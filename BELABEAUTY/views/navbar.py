import flet as ft

def NavBar(page: ft.Page):
    return ft.Container(
        content=ft.Row(
            [
                # Título clickeable que lleva al inicio
                ft.TextButton(
                    content=ft.Text(
                        "BELA BEAUTY",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK
                    ),
                    on_click=lambda e: page.go("/")
                ),

                # Botones del menú
                ft.Row(
                    [
                        ft.TextButton("Servicios", on_click=lambda e: page.go("/servicios")),
                        ft.TextButton("Horarios", on_click=lambda e: page.go("/horarios")),
                        ft.TextButton("Contacto", on_click=lambda e: page.go("/contacto")),
                        ft.TextButton("Ubicación", on_click=lambda e: page.go("/ubicacion")),
                    ],
                    spacing=10
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.symmetric(horizontal=30, vertical=15),
        bgcolor=ft.Colors.WHITE,
        border_radius=5
    )