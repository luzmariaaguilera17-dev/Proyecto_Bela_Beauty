import flet as ft
from views.navbar import NavBar

class ServiciosView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/servicios", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Datos de servicios - cada uno con: nombre, precio, duración, imagen, ruta
        servicios = [
            {
                "nombre": "Uñas Acrílicas",
                "descripcion": "Polygel, Uñas en Gel, Semipermanentes",
                "precio": "Desde 35 USD",
                "duracion": "90 min",
                "imagen": "acrilicas.jpeg",  # Cambia por tu imagen
                "ruta": "/servicios/acrilicas"
            },
            {
                "nombre": "Semipermanente",
                "descripcion": "Esmaltado de larga duración",
                "precio": "25 USD",
                "duracion": "60 min",
                "imagen": "semipermanentes.jpeg",  # Cambia por tu imagen
                "ruta": "/servicios/semipermanente"
            },
            {
                "nombre": "Manicura Simple",
                "descripcion": "Corte, limado y esmaltado básico",
                "precio": "15 USD",
                "duracion": "45 min",
                "imagen": "gel.jpeg",  # Cambia por tu imagen
                "ruta": "/servicios/manicura"
            },
            {
                "nombre": "Nail Art",
                "descripcion": "Decoración personalizada",
                "precio": "10-20 USD",
                "duracion": "30-45 min",
                "imagen": "polygel.jpeg",  # Cambia por tu imagen
                "ruta": "/servicios/nailart"
            }
        ]

        def crear_tarjeta_servicio(servicio):
            """Crea una tarjeta para cada servicio"""
            return ft.Container(
                content=ft.Column(
                    [
                        # Imagen del servicio
                        ft.Container(
                            ft.Image(
                                src=servicio["imagen"],
                                fit=ft.ImageFit.COVER,
                                width=280,
                                height=200,
                                border_radius=ft.border_radius.all(12)
                            ),
                            bgcolor=ft.Colors.WHITE,
                            border_radius=12,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.Colors.BLACK12,
                            ),
                            alignment=ft.alignment.center,
                        ),
                        
                        # Título del servicio
                        ft.Container(
                            ft.Column([
                                ft.Text(
                                    servicio["nombre"],
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    servicio["descripcion"],
                                    size=14,
                                    color=ft.Colors.GREY_700,
                                    text_align=ft.TextAlign.CENTER
                                ),
                            ]),
                            padding=ft.padding.symmetric(horizontal=10)
                        ),
                        
                        # Información de precio y duración
                        ft.Row([
                            ft.Column([
                                ft.Text("PRECIO", size=12, color=ft.Colors.GREY_600),
                                ft.Text(servicio["precio"], size=16, weight=ft.FontWeight.W_600),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.VerticalDivider(),
                            ft.Column([
                                ft.Text("DURACIÓN", size=12, color=ft.Colors.GREY_600),
                                ft.Text(servicio["duracion"], size=16, weight=ft.FontWeight.W_600),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                        
                        # Botón de Ver Detalles
                        ft.Container(
                            ft.ElevatedButton(
                                text="Ver Detalles",
                                icon=ft.Icons.ARROW_FORWARD,
                                on_click=lambda e, r=servicio["ruta"]: self.page.go(r),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.AMBER_200,
                                    color=ft.Colors.BLACK,
                                )
                            ),
                            padding=ft.padding.only(top=10)
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
                width=320,
                padding=15,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.BLACK12,
                ),
                margin=10,
            )

        # Crear las tarjetas de servicios
        tarjetas_servicios = ft.Row(
            [
                crear_tarjeta_servicio(servicio) for servicio in servicios
            ],
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            run_spacing=20,
        )

        # Título principal
        titulo_principal = ft.Container(
            content=ft.Column([
                ft.Text(
                    "BELA BEAUTY",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.AMBER_800
                ),
                ft.Text(
                    "NAILS",
                    size=24,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.AMBER_700
                ),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Text(
                    "TRABAJOS REALIZADOS",
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.GREY_700
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(bottom=30)
        )

        # Sección de información adicional
        info_adicional = ft.Container(
            content=ft.Column([
                ft.Divider(),
                ft.Text(
                    "¿Deseas reservar un servicio? Ve a la sección Horarios.",
                    size=16,
                    italic=True,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.ElevatedButton(
                    "Reservar Ahora",
                    on_click=lambda e: self.page.go("/horarios"),
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.AMBER_200,
                        color=ft.Colors.BLACK,
                        padding=ft.padding.symmetric(horizontal=30, vertical=15)
                    )
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
            padding=20,
            margin=ft.margin.only(top=30)
        )

        # Construir la vista completa
        self.controls = [
            ft.Column(
                [
                    NavBar(self.page),
                    ft.Container(
                        content=ft.Column(
                            [
                                titulo_principal,
                                tarjetas_servicios,
                                info_adicional
                            ],
                            scroll=ft.ScrollMode.AUTO,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        expand=True
                    )
                ],
                spacing=0,
                expand=True
            )
        ]