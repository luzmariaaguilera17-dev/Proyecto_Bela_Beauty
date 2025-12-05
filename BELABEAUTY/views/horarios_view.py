import flet as ft
from views.navbar import NavBar
import datetime

class HorariosView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/horarios", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Estado para la selección de horario
        self.horario_seleccionado = None
        self.dia_seleccionado = None
        
        # Campos del formulario
        nombre_field = ft.TextField(
            label="Nombre",
            width=400,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        email_field = ft.TextField(
            label="Email",
            width=195,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        telefono_field = ft.TextField(
            label="Número de Teléfono",
            width=195,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
        )
        
        # Contenedor para email y teléfono en fila
        contacto_row = ft.Row(
            [email_field, telefono_field],
            spacing=10
        )
        
        # Función para manejar selección de horario
        def seleccionar_horario(dia, hora, e):
            # Resetear todos los botones a color normal
            for container in horarios_container.content.controls:
                for row in container.content.controls[1].controls:
                    if isinstance(row, ft.Row):
                        for btn in row.controls:
                            if isinstance(btn, ft.Container):
                                btn.bgcolor = ft.Colors.WHITE
                                btn.border = ft.border.all(1, ft.Colors.GREY_300)
            
            # Cambiar color del botón seleccionado
            e.control.bgcolor = ft.Colors.AMBER_200
            e.control.border = ft.border.all(2, ft.Colors.AMBER_600)
            
            # Guardar selección
            self.horario_seleccionado = hora
            self.dia_seleccionado = dia
            
            # Actualizar mensaje
            confirmacion_text.value = f"Cita seleccionada: {dia} a las {hora}"
            self.page.update()
        
        # Función para agendar cita
        def agendar_cita(e):
            if not nombre_field.value:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Por favor ingresa tu nombre"),
                    bgcolor=ft.Colors.RED_400
                )
                self.page.snack_bar.open = True
            elif not self.horario_seleccionado:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Por favor selecciona un horario"),
                    bgcolor=ft.Colors.RED_400
                )
                self.page.snack_bar.open = True
            else:
                # Aquí normalmente enviarías los datos a un servidor
                self.page.snack_bar = ft.SnackBar(
                    ft.Text(f"¡Cita agendada para {self.dia_seleccionado} a las {self.horario_seleccionado}!"),
                    bgcolor=ft.Colors.GREEN_400
                )
                self.page.snack_bar.open = True
                
                # Limpiar formulario
                nombre_field.value = ""
                email_field.value = ""
                telefono_field.value = ""
                self.horario_seleccionado = None
                self.dia_seleccionado = None
                confirmacion_text.value = "Selecciona un horario"
                
                # Resetear botones de horario
                for container in horarios_container.content.controls:
                    for row in container.content.controls[1].controls:
                        if isinstance(row, ft.Row):
                            for btn in row.controls:
                                if isinstance(btn, ft.Container):
                                    btn.bgcolor = ft.Colors.WHITE
                                    btn.border = ft.border.all(1, ft.Colors.GREY_300)
            
            self.page.update()
        
        # Horarios disponibles por día
        horarios_por_dia = {
            "Lunes": ["8:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
            "Martes": ["9:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
            "Miércoles": ["8:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
            "Jueves": ["9:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
            "Viernes": ["9:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
            "Sábado": ["9:00am", "10:00am", "11:00am", "12:00pm", "3:00pm", "4:00pm", "5:00pm", "6:00pm"],
        }
        
        # Función para crear botones de horario
        def crear_boton_horario(dia, hora):
            return ft.Container(
                content=ft.Text(
                    hora,
                    size=12,
                    weight=ft.FontWeight.W_500,
                    text_align=ft.TextAlign.CENTER
                ),
                width=70,
                height=35,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=8,
                alignment=ft.alignment.center,
                on_click=lambda e, d=dia, h=hora: seleccionar_horario(d, h, e)
            )
        
        # Crear contenedores para cada par de días
        pares_dias = [
            ("Lunes", "Jueves"),
            ("Martes", "Viernes"),
            ("Miércoles", "Sábado")
        ]
        
        horarios_containers = []
        
        for dia1, dia2 in pares_dias:
            # Primera fila de horarios (mañana)
            fila_manana1 = ft.Row(
                [crear_boton_horario(dia1, h) for h in horarios_por_dia[dia1][:4]],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            fila_manana2 = ft.Row(
                [crear_boton_horario(dia2, h) for h in horarios_por_dia[dia2][:4]],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            # Segunda fila de horarios (tarde)
            fila_tarde1 = ft.Row(
                [crear_boton_horario(dia1, h) for h in horarios_por_dia[dia1][4:]],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            fila_tarde2 = ft.Row(
                [crear_boton_horario(dia2, h) for h in horarios_por_dia[dia2][4:]],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER
            )
            
            container = ft.Container(
                content=ft.Column(
                    [
                        # Título del par de días
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text(
                                        dia1,
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.AMBER_800
                                    ),
                                    width=150,
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        dia2,
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.AMBER_800
                                    ),
                                    width=150,
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        
                        # Horarios de mañana
                        ft.Row(
                            [
                                ft.Column([fila_manana1], width=150, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                ft.Column([fila_manana2], width=150, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ],
                            spacing=20
                        ),
                        
                        # Espacio
                        ft.Container(height=10),
                        
                        # Horarios de tarde
                        ft.Row(
                            [
                                ft.Column([fila_tarde1], width=150, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                ft.Column([fila_tarde2], width=150, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ],
                            spacing=20
                        )
                    ],
                    spacing=10
                ),
                padding=15,
                bgcolor=ft.Colors.AMBER_50,
                border_radius=15,
                margin=ft.margin.only(bottom=20)
            )
            
            horarios_containers.append(container)
        
        # Contenedor principal de horarios
        horarios_container = ft.Container(
            content=ft.Column(
                horarios_containers,
                spacing=0
            )
        )
        
        # Texto de confirmación
        confirmacion_text = ft.Text(
            "Selecciona un horario",
            size=16,
            weight=ft.FontWeight.W_500,
            color=ft.Colors.GREY_700,
            text_align=ft.TextAlign.CENTER
        )
        
        # Construir la vista completa
        self.controls = [
            ft.Column(
                [
                    NavBar(self.page),
                    
                    # Título principal
                    ft.Container(
                        content=ft.Text(
                            "AGENDA TU CITA",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.AMBER_800,
                            text_align=ft.TextAlign.CENTER
                        ),
                        margin=ft.margin.only(bottom=10, top=20)
                    ),
                    
                    # Formulario
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("NOMBRE", size=14, weight=ft.FontWeight.W_600, color=ft.Colors.GREY_700),
                                nombre_field,
                                ft.Container(height=15),
                                ft.Text("CONTACTO", size=14, weight=ft.FontWeight.W_600, color=ft.Colors.GREY_700),
                                contacto_row,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        width=420,
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=15,
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=10,
                            color=ft.Colors.BLACK12,
                        ),
                        margin=ft.margin.only(bottom=30)
                    ),
                    
                    # Título de horarios
                    ft.Container(
                        content=ft.Text(
                            "Horarios disponibles",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.AMBER_700,
                            text_align=ft.TextAlign.CENTER
                        ),
                        margin=ft.margin.only(bottom=20)
                    ),
                    
                    # Horarios
                    horarios_container,
                    
                    # Confirmación
                    ft.Container(
                        content=confirmacion_text,
                        margin=ft.margin.only(bottom=20)
                    ),
                    
                    # Botón de agendar
                    ft.Container(
                        ft.ElevatedButton(
                            "AGENDAR",
                            on_click=agendar_cita,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.AMBER_200,
                                color=ft.Colors.BLACK,
                                padding=ft.padding.symmetric(horizontal=40, vertical=20),
                                elevation=5
                            ),
                            icon=ft.Icons.CALENDAR_MONTH,
                            icon_color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(bottom=40)
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                expand=True
            )
        ]