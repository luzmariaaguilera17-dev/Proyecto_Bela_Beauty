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
                ft.Container(height=40),
                
                # Fila con dos columnas: logo a la izquierda, contenido a la derecha
                ft.Row([
                    # Columna izquierda: Logo grande cuadrado
                    ft.Column([
                        ft.Container(
                            ft.Image(
                                src="logo.png",  # Cambia a "assets/logo.png" si está en la carpeta assets
                                fit=ft.ImageFit.COVER,
                                width=400,
                                height=400
                            ),
                            width=420,
                            height=420,
                            bgcolor=ft.Colors.WHITE,
                            border_radius=20,
                            padding=ft.padding.all(10),
                            shadow=ft.BoxShadow(
                                spread_radius=2,
                                blur_radius=40,
                                color=ft.Colors.BLACK26,
                            ),
                            border=ft.border.all(3, ft.Colors.AMBER_100),
                            clip_behavior=ft.ClipBehavior.HARD_EDGE
                        )
                    ], 
                    width=450,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    
                    # Columna derecha: Título y botón
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                ft.Text(
                                    "BELA BEAUTY",
                                    size=64,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.AMBER_800,
                                    text_align=ft.TextAlign.LEFT
                                ),
                                ft.Container(height=10),
                                ft.Text(
                                    "Salon & Nails",
                                    size=32,
                                    color=ft.Colors.AMBER_600,
                                    text_align=ft.TextAlign.LEFT
                                ),
                                ft.Container(height=30),
                                ft.Text(
                                    "Transformando belleza en confianza desde 2020",
                                    size=20,
                                    color=ft.Colors.GREY_600,
                                    text_align=ft.TextAlign.LEFT,
                                    italic=True
                                ),
                                ft.Container(height=60),
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Saber más sobre la dueña",
                                        on_click=go_next,
                                        icon=ft.Icons.ACCOUNT_CIRCLE,
                                        icon_color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.AMBER_200,
                                            color=ft.Colors.BLACK,
                                            padding=ft.padding.symmetric(horizontal=40, vertical=22),
                                            elevation=5,
                                            shape=ft.RoundedRectangleBorder(radius=15),
                                        ),
                                    ),
                                    alignment=ft.alignment.center_left
                                ),
                                ft.Container(height=30),
                                ft.Row([
                                    ft.Icon(ft.Icons.STAR, color=ft.Colors.AMBER_300),
                                    ft.Text("  Manicura profesional", size=16, color=ft.Colors.GREY_600),
                                ]),
                                ft.Container(height=5),
                                ft.Row([
                                    ft.Icon(ft.Icons.STAR, color=ft.Colors.AMBER_300),
                                    ft.Text("  Uñas acrílicas y gel", size=16, color=ft.Colors.GREY_600),
                                ]),
                                ft.Container(height=5),
                                ft.Row([
                                    ft.Icon(ft.Icons.STAR, color=ft.Colors.AMBER_300),
                                    ft.Text("  Diseños personalizados", size=16, color=ft.Colors.GREY_600),
                                ]),
                            ]),
                            padding=ft.padding.only(left=40),
                            width=450
                        )
                    ], 
                    width=450,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH)
                ], 
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                wrap=True),
                
                # Pie de página
                ft.Container(
                    ft.Text(
                        "¡Reserva tu cita hoy mismo!",
                        size=18,
                        color=ft.Colors.AMBER_700,
                        weight=ft.FontWeight.W_500,
                        text_align=ft.TextAlign.CENTER
                    ),
                    padding=ft.padding.all(30),
                    margin=ft.margin.only(top=40)
                )
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO)
        ]