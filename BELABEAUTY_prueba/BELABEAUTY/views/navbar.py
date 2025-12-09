import flet as ft

class NavBar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.build_navbar()
    
    def navigate_to(self, e, route):
        """Función para navegar a diferentes vistas"""
        self.page.go(route)
    
    def build_navbar(self):
        # Crear botones de navegación
        btn_inicio = ft.ElevatedButton(
            "Inicio",
            on_click=lambda e: self.navigate_to(e, "/")
        )
        
        btn_servicios = ft.ElevatedButton(
            "Servicios",
            on_click=lambda e: self.navigate_to(e, "/servicios")
        )
        
        btn_horarios = ft.ElevatedButton(
            "Horarios",
            on_click=lambda e: self.navigate_to(e, "/horarios")
        )
        
        btn_contacto = ft.ElevatedButton(
            "Contacto",
            on_click=lambda e: self.navigate_to(e, "/contacto")
        )
        
        btn_ubicacion = ft.ElevatedButton(
            "Ubicación",
            on_click=lambda e: self.navigate_to(e, "/ubicacion")
        )
        
        # Crear la fila de botones
        nav_row = ft.Row(
            controls=[
                btn_inicio,
                btn_servicios,
                btn_horarios,
                btn_contacto,
                btn_ubicacion
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
        
        # Configurar el contenedor de la barra de navegación
        self.content = nav_row
        self.bgcolor = ft.Colors.AMBER_50
        self.padding = ft.padding.all(20)
        self.border_radius = 10
        self.margin = ft.margin.only(bottom=20)