import flet as ft
import re
from views.navbar import NavBar
from db import (
    crear_cita, obtener_citas, obtener_cita_por_id, 
    actualizar_cita, cambiar_estado_cita  # Quitamos eliminar_cita
)

class HorariosView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__("/horarios", controls=[])
        self.page = page
        self.modo_edicion = False
        self.cita_id_editar = None
        # Referencias a controles importantes
        self.nombre_field = None
        self.email_field = None
        self.telefono_field = None
        self.confirmacion_text = None
        self.boton_accion_principal = None
        self.boton_cancelar = None
        self.contenedor_botones = None
        self.boton_seleccionado = None
        self.horario_seleccionado = None
        self.dia_seleccionado = None
        self.tabla_citas_container = None
        self.mensaje_exito_container = None
        self.mensaje_tabla_container = None  # Nuevo contenedor para mensajes de la tabla
        self.build_view()

    def build_view(self):
        # Campos del formulario
        self.nombre_field = ft.TextField(
            label="Nombre completo",
            width=300,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            text_size=14,
            hint_text="Ej: Juana Pérez",
            prefix_icon=ft.Icons.PERSON,
            on_change=lambda e: self.limpiar_error_nombre()
        )
        
        self.email_field = ft.TextField(
            label="Email",
            width=145,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            text_size=14,
            hint_text="ejemplo@email.com",
            prefix_icon=ft.Icons.EMAIL,
            on_change=lambda e: self.limpiar_error_email()
        )
        
        self.telefono_field = ft.TextField(
            label="Teléfono",
            width=145,
            filled=True,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            text_size=14,
            hint_text="Ej: 0985223516",
            prefix_icon=ft.Icons.PHONE,
            on_change=lambda e: self.limpiar_error_telefono()
        )
        
        # Mensajes de error para cada campo
        self.error_nombre = ft.Text("", size=11, color=ft.Colors.RED_400, visible=False)
        self.error_email = ft.Text("", size=11, color=ft.Colors.RED_400, visible=False)
        self.error_telefono = ft.Text("", size=11, color=ft.Colors.RED_400, visible=False)
        self.error_horario = ft.Text("", size=11, color=ft.Colors.RED_400, visible=False)
        
        # Contenedor para email y teléfono
        contacto_row = ft.Row([self.email_field, self.telefono_field], spacing=10)
        
        # Texto de confirmación
        self.confirmacion_text = ft.Text(
            "Selecciona un horario de la tabla",
            size=14,
            weight=ft.FontWeight.W_500,
            color=ft.Colors.GREY_700,
            text_align=ft.TextAlign.CENTER
        )
        
        # Contenedor para mensajes de éxito del formulario
        self.mensaje_exito_container = ft.Container(
            content=ft.Column([], spacing=0),
            visible=False,
            animate_opacity=300,
            margin=ft.margin.only(bottom=10)
        )
        
        # Contenedor para mensajes de éxito de la tabla (debajo de "Gestiona tus citas existentes")
        self.mensaje_tabla_container = ft.Container(
            content=ft.Column([], spacing=0),
            visible=False,
            animate_opacity=300,
            margin=ft.margin.only(bottom=15)
        )
        
        # Botón de acción principal
        self.boton_accion_principal = ft.ElevatedButton(
            "AGENDAR CITA",
            on_click=self.agendar_cita_handler,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.AMBER_400,
                color=ft.Colors.WHITE,
                padding=ft.padding.symmetric(horizontal=35, vertical=12),
                elevation=3,
                shape=ft.RoundedRectangleBorder(radius=8)
            ),
            icon=ft.Icons.CALENDAR_MONTH,
            icon_color=ft.Colors.WHITE,
            width=200
        )
        
        # Botón para cancelar edición (oculto inicialmente)
        self.boton_cancelar = ft.OutlinedButton(
            "Cancelar",
            on_click=self.cancelar_edicion_handler,
            style=ft.ButtonStyle(
                color=ft.Colors.RED_400,
                shape=ft.RoundedRectangleBorder(radius=8)
            ),
            width=100,
            visible=False
        )
        
        # Contenedor de botones
        self.contenedor_botones = ft.Row(
            [self.boton_accion_principal, self.boton_cancelar],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        
        # Horarios disponibles
        horarios_por_dia = {
            "Lunes": ["8:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
            "Martes": ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
            "Miércoles": ["8:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
            "Jueves": ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
            "Viernes": ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
            "Sábado": ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"],
        }
        
        # Función para crear botones de horario
        def crear_boton_horario(dia, hora):
            return ft.Container(
                content=ft.Text(
                    hora,
                    size=11,
                    weight=ft.FontWeight.W_500,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BLACK
                ),
                width=60,
                height=35,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=8,
                alignment=ft.alignment.center,
                on_click=lambda e, d=dia, h=hora: self.seleccionar_horario_handler(d, h, e)
            )
        
        # Crear tabla de horarios
        horarios_rows = []
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        
        # Fila de encabezados
        headers = []
        for dia in dias_semana:
            headers.append(
                ft.Container(
                    content=ft.Text(
                        dia[:3],
                        size=13,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_800,
                        text_align=ft.TextAlign.CENTER
                    ),
                    width=75,
                    padding=6,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.AMBER_100,
                    border_radius=8
                )
            )
        
        horarios_rows.append(
            ft.Container(
                content=ft.Row(headers, spacing=3, alignment=ft.MainAxisAlignment.CENTER),
                padding=ft.padding.only(bottom=10)
            )
        )
        
        # Crear filas de horarios
        for i in range(8):
            row_horarios = []
            for dia in dias_semana:
                hora = horarios_por_dia[dia][i]
                row_horarios.append(crear_boton_horario(dia, hora))
            
            # Separador mañana/tarde
            if i == 4:
                horarios_rows.append(
                    ft.Container(
                        content=ft.Text("Tarde", size=12, weight=ft.FontWeight.W_600, 
                                       color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                        padding=ft.padding.only(top=10, bottom=5)
                    )
                )
            
            horarios_rows.append(
                ft.Container(
                    content=ft.Row(row_horarios, spacing=3, alignment=ft.MainAxisAlignment.CENTER),
                    padding=ft.padding.only(bottom=5)
                )
            )
        
        # Contenedor principal de horarios
        horarios_container = ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Text("Mañana", size=12, weight=ft.FontWeight.W_600, 
                                       color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                        padding=ft.padding.only(bottom=5)
                    )
                ] + horarios_rows,
                spacing=0,
                scroll=ft.ScrollMode.AUTO
            ),
            width=550,
            height=450,
            padding=12,
            bgcolor=ft.Colors.AMBER_50,
            border_radius=12,
            margin=ft.margin.only(bottom=20)
        )
        
        # Crear tabla de citas
        self.tabla_citas_container = self.crear_tabla_citas()
        
        # Construir la vista completa
        self.controls = [
            ft.Column(
                [
                    NavBar(self.page),
                    
                    # Título principal
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("AGENDA TU CITA", size=26, weight=ft.FontWeight.BOLD,
                                       color=ft.Colors.AMBER_800, text_align=ft.TextAlign.CENTER),
                                ft.Text("Selecciona un horario disponible", size=13,
                                       color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)
                            ]
                        ),
                        margin=ft.margin.only(bottom=15, top=15)
                    ),
                    
                    # Contenedor principal con dos columnas
                    ft.Container(
                        content=ft.Row(
                            [
                                # Columna izquierda: Formulario
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            # Mensaje de éxito en la parte superior
                                            self.mensaje_exito_container,
                                            
                                            ft.Text("Información Personal", size=16,
                                                   weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_700,
                                                   text_align=ft.TextAlign.CENTER),
                                            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                            
                                            # Campo Nombre
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text("Nombre completo *", size=12,
                                                               weight=ft.FontWeight.W_600, color=ft.Colors.GREY_700),
                                                        self.nombre_field,
                                                        self.error_nombre
                                                    ],
                                                    spacing=2
                                                ),
                                                width=300
                                            ),
                                            
                                            ft.Container(height=10),
                                            
                                            # Campo Contacto
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Text("Contacto *", size=12,
                                                               weight=ft.FontWeight.W_600, color=ft.Colors.GREY_700),
                                                        contacto_row
                                                    ],
                                                    spacing=2
                                                ),
                                                width=300
                                            ),
                                            
                                            # Errores de email y teléfono
                                            ft.Container(
                                                content=ft.Column(
                                                    [self.error_email, self.error_telefono],
                                                    spacing=2
                                                ),
                                                width=300,
                                                padding=ft.padding.only(top=5)
                                            ),
                                            
                                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                                            
                                            # Confirmación de horario
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        self.confirmacion_text,
                                                        self.error_horario
                                                    ],
                                                    spacing=2
                                                ),
                                                width=300,
                                                padding=ft.padding.symmetric(vertical=10),
                                                bgcolor=ft.Colors.GREY_100,
                                                border_radius=8,
                                                alignment=ft.alignment.center
                                            ),
                                            
                                            ft.Container(height=15),
                                            
                                            # Botones de acción
                                            self.contenedor_botones,
                                            
                                            # Texto de instrucciones
                                            ft.Container(
                                                content=ft.Text(
                                                    "* Campos obligatorios",
                                                    size=10,
                                                    color=ft.Colors.GREY_500,
                                                    text_align=ft.TextAlign.CENTER
                                                ),
                                                padding=ft.padding.only(top=10)
                                            )
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=0
                                    ),
                                    width=320,
                                    padding=15,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=12,
                                    shadow=ft.BoxShadow(spread_radius=1, blur_radius=8, color=ft.Colors.BLACK12)
                                ),
                                
                                ft.Container(width=15),
                                
                                # Columna derecha: Horarios
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text("Horarios Disponibles *", size=16,
                                                   weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_700,
                                                   text_align=ft.TextAlign.CENTER),
                                            ft.Text("Haz clic en un horario para seleccionarlo", size=11,
                                                   color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                                            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                            horarios_container,
                                            ft.Text("⏰ Horarios en formato de 24 horas", size=9,
                                                   color=ft.Colors.GREY_500, text_align=ft.TextAlign.CENTER)
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=0
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START
                        ),
                        margin=ft.margin.only(bottom=30, left=10, right=10)
                    ),
                    
                    # Título de citas existentes
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Citas Agendadas", size=22, weight=ft.FontWeight.BOLD,
                                       color=ft.Colors.AMBER_700, text_align=ft.TextAlign.CENTER),
                                ft.Text("Gestiona tus citas existentes", size=12,
                                       color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                                # Mensaje de éxito para operaciones de tabla
                                self.mensaje_tabla_container
                            ]
                        ),
                        margin=ft.margin.only(bottom=20, top=20)
                    ),
                    
                    # Tabla de citas
                    self.tabla_citas_container
                ],
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                expand=True
            )
        ]
    
    # ========== FUNCIONES PARA LIMPIAR ERRORES ==========
    
    def limpiar_error_nombre(self):
        self.error_nombre.value = ""
        self.error_nombre.visible = False
        self.page.update()
    
    def limpiar_error_email(self):
        self.error_email.value = ""
        self.error_email.visible = False
        self.page.update()
    
    def limpiar_error_telefono(self):
        self.error_telefono.value = ""
        self.error_telefono.visible = False
        self.page.update()
    
    def limpiar_error_horario(self):
        self.error_horario.value = ""
        self.error_horario.visible = False
        self.page.update()
    
    # ========== FUNCIONES PARA MOSTRAR MENSAJES DE ÉXITO ==========
    
    def mostrar_mensaje_exito(self, mensaje, tipo="guardar", ubicacion="formulario"):
        """Muestra un mensaje de éxito en la ubicación especificada"""
        # Definir icono y color según el tipo
        if tipo == "guardar":
            icono = ft.Icons.CHECK_CIRCLE
            color = ft.Colors.GREEN_500
            bg_color = ft.Colors.GREEN_50
            titulo = "¡CITA GUARDADA CON ÉXITO!"
        elif tipo == "editar":
            icono = ft.Icons.EDIT
            color = ft.Colors.BLUE_500
            bg_color = ft.Colors.BLUE_50
            titulo = "¡CITA EDITADA CON ÉXITO!"
        elif tipo == "cancelar":
            icono = ft.Icons.CANCEL
            color = ft.Colors.ORANGE_500
            bg_color = ft.Colors.ORANGE_50
            titulo = "¡CITA CANCELADA!"
        elif tipo == "confirmar":
            icono = ft.Icons.CHECK_CIRCLE
            color = ft.Colors.GREEN_500
            bg_color = ft.Colors.GREEN_50
            titulo = "¡CITA CONFIRMADA!"
        elif tipo == "pendiente":
            icono = ft.Icons.SCHEDULE
            color = ft.Colors.AMBER_500
            bg_color = ft.Colors.AMBER_50
            titulo = "¡CITA MARCADA COMO PENDIENTE!"
        else:
            icono = ft.Icons.CHECK_CIRCLE
            color = ft.Colors.GREEN_500
            bg_color = ft.Colors.GREEN_50
            titulo = mensaje
        
        # Crear el contenido del mensaje
        contenido = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icono, color=color, size=24),
                    ft.Column(
                        [
                            ft.Text(titulo, size=14, weight=ft.FontWeight.BOLD, color=color),
                            ft.Text(mensaje, size=12, color=ft.Colors.GREY_700),
                        ],
                        spacing=2
                    )
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.START
            ),
            padding=15,
            bgcolor=bg_color,
            border_radius=10,
            border=ft.border.all(1.5, color),
            width=900 if ubicacion == "tabla" else 300,
            animate_opacity=300
        )
        
        # Determinar en qué contenedor mostrar el mensaje
        if ubicacion == "formulario":
            contenedor = self.mensaje_exito_container
        else:  # ubicacion == "tabla"
            contenedor = self.mensaje_tabla_container
        
        # Actualizar el contenedor de mensajes
        contenedor.content.controls = [contenido]
        contenedor.visible = True
        contenedor.opacity = 1
        
        # Auto-ocultar después de 5 segundos
        import threading
        def ocultar_mensaje():
            import time
            time.sleep(5)
            contenedor.visible = False
            self.page.update()
        
        threading.Thread(target=ocultar_mensaje, daemon=True).start()
        
        self.page.update()
    
    # ========== VALIDACIONES ==========
    
    def validar_nombre(self, nombre):
        """Valida que el nombre contenga solo letras y espacios"""
        nombre = nombre.strip()
        
        if not nombre:
            return False, "El nombre no puede estar vacío"
        
        # Permitir letras, espacios, acentos y la letra ñ
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', nombre):
            return False, "Formato incorrecto. Solo letras y espacios"
        
        if len(nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"
        
        return True, ""

    def validar_email(self, email):
        """Valida el formato del email"""
        email = email.strip()
        
        if not email:
            return False, "El email no puede estar vacío"
        
        # Expresión regular para validar email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            return False, "Formato de email incorrecto"
        
        return True, ""

    def validar_telefono(self, telefono):
        """Valida el formato del teléfono"""
        telefono = telefono.strip()
        
        if not telefono:
            return False, "El teléfono no puede estar vacío"
        
        # Remover espacios, guiones, paréntesis
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        
        # Validar que solo contenga números
        if not telefono_limpio.isdigit():
            return False, "Formato incorrecto. Solo números"
        
        # Validar longitud
        if len(telefono_limpio) < 10:
            return False, "Mínimo 10 dígitos"
        
        if len(telefono_limpio) > 15:
            return False, "Máximo 15 dígitos"
        
        return True, ""
    
    def validar_horario(self):
        """Valida que se haya seleccionado un horario"""
        if not self.horario_seleccionado or not self.dia_seleccionado:
            return False, "Debes seleccionar un horario"
        return True, ""
    
    # ========== HANDLERS ==========
    
    def seleccionar_horario_handler(self, dia, hora, e):
        """Maneja la selección de un horario"""
        # Resetear el botón previamente seleccionado si existe
        if self.boton_seleccionado:
            self.boton_seleccionado.bgcolor = ft.Colors.WHITE
            self.boton_seleccionado.border = ft.border.all(1, ft.Colors.GREY_300)
        
        # Cambiar color del botón seleccionado
        e.control.bgcolor = ft.Colors.AMBER_400
        e.control.border = ft.border.all(2, ft.Colors.AMBER_700)
        
        # Guardar referencia al botón seleccionado
        self.boton_seleccionado = e.control
        
        # Guardar selección
        self.horario_seleccionado = hora
        self.dia_seleccionado = dia
        
        # Limpiar error de horario
        self.limpiar_error_horario()
        
        # Actualizar mensaje
        self.confirmacion_text.value = f"✅ Cita seleccionada: {dia} a las {hora}"
        self.confirmacion_text.color = ft.Colors.GREEN_600
        
        # Ocultar mensajes de éxito
        self.mensaje_exito_container.visible = False
        self.mensaje_tabla_container.visible = False
        
        self.page.update()
    
    def agendar_cita_handler(self, e):
        """Maneja el agendamiento o actualización de una cita"""
        # Ocultar mensajes de éxito anteriores
        self.mensaje_exito_container.visible = False
        self.mensaje_tabla_container.visible = False
        
        # Limpiar errores anteriores
        self.limpiar_error_nombre()
        self.limpiar_error_email()
        self.limpiar_error_telefono()
        self.limpiar_error_horario()
        
        # Validar todos los campos
        nombre_valido, error_nombre = self.validar_nombre(self.nombre_field.value)
        email_valido, error_email = self.validar_email(self.email_field.value)
        telefono_valido, error_telefono = self.validar_telefono(self.telefono_field.value)
        horario_valido, error_horario = self.validar_horario()
        
        # Mostrar errores específicos
        if not nombre_valido:
            self.error_nombre.value = f"⚠️ {error_nombre}"
            self.error_nombre.visible = True
        
        if not email_valido:
            self.error_email.value = f"⚠️ {error_email}"
            self.error_email.visible = True
        
        if not telefono_valido:
            self.error_telefono.value = f"⚠️ {error_telefono}"
            self.error_telefono.visible = True
        
        if not horario_valido:
            self.error_horario.value = f"⚠️ {error_horario}"
            self.error_horario.visible = True
        
        # Si hay errores, no continuar
        if not all([nombre_valido, email_valido, telefono_valido, horario_valido]):
            self.page.update()
            return
        
        try:
            if self.modo_edicion and self.cita_id_editar:
                # Actualizar cita existente
                actualizar_cita(
                    self.cita_id_editar,
                    self.nombre_field.value.strip(),
                    self.email_field.value.strip(),
                    self.telefono_field.value.strip(),
                    self.dia_seleccionado,
                    self.horario_seleccionado
                )
                
                # Mostrar mensaje de éxito en el formulario
                detalle = f"{self.dia_seleccionado} a las {self.horario_seleccionado}"
                self.mostrar_mensaje_exito(detalle, "editar", "formulario")
                
                # Resetear modo edición
                self.modo_edicion = False
                self.cita_id_editar = None
                
                # Cambiar botón a "AGENDAR CITA"
                self.cambiar_modo_formulario("agendar")
            else:
                # Crear nueva cita
                cita_id = crear_cita(
                    self.nombre_field.value.strip(),
                    self.email_field.value.strip(),
                    self.telefono_field.value.strip(),
                    self.dia_seleccionado,
                    self.horario_seleccionado
                )
                
                # Mostrar mensaje de éxito en el formulario
                detalle = f"ID: {cita_id} - {self.dia_seleccionado} a las {self.horario_seleccionado}"
                self.mostrar_mensaje_exito(detalle, "guardar", "formulario")
            
            # Limpiar formulario
            self.limpiar_formulario()
            
            # Actualizar tabla
            self.actualizar_tabla_citas()
            
        except Exception as ex:
            # Mostrar mensaje de error
            self.mostrar_mensaje_error(f"Error: {str(ex)}", "formulario")
    
    def mostrar_mensaje_error(self, mensaje, ubicacion="formulario"):
        """Muestra un mensaje de error"""
        contenido = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED_500, size=24),
                    ft.Column(
                        [
                            ft.Text("¡ERROR!", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_600),
                            ft.Text(mensaje, size=12, color=ft.Colors.RED_600),
                        ],
                        spacing=2
                    )
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.START
            ),
            padding=15,
            bgcolor=ft.Colors.RED_50,
            border_radius=10,
            border=ft.border.all(1.5, ft.Colors.RED_300),
            width=900 if ubicacion == "tabla" else 300
        )
        
        # Determinar en qué contenedor mostrar el mensaje
        if ubicacion == "formulario":
            contenedor = self.mensaje_exito_container
        else:  # ubicacion == "tabla"
            contenedor = self.mensaje_tabla_container
        
        contenedor.content.controls = [contenido]
        contenedor.visible = True
        self.page.update()
    
    def cancelar_edicion_handler(self, e):
        """Cancela el modo de edición"""
        self.modo_edicion = False
        self.cita_id_editar = None
        
        self.limpiar_formulario()
        self.cambiar_modo_formulario("agendar")
        
        # Mostrar mensaje informativo
        self.mostrar_mensaje_exito("Edición cancelada", "guardar", "formulario")
    
    # ========== FUNCIONES CRUD ==========
    
    def cargar_cita_para_editar(self, id_cita):
        """Carga una cita existente en el formulario para editar"""
        cita = obtener_cita_por_id(id_cita)
        
        if cita:
            id_cita, nombre, email, telefono, dia, hora, estado, fecha_creacion, fecha_actualizacion = cita
            
            # Llenar formulario con datos de la cita
            self.nombre_field.value = nombre
            self.email_field.value = email
            self.telefono_field.value = telefono
            self.dia_seleccionado = dia
            self.horario_seleccionado = hora
            
            # Establecer modo edición
            self.modo_edicion = True
            self.cita_id_editar = id_cita
            
            # Actualizar texto de confirmación
            self.confirmacion_text.value = f"✏️ Editando cita: {dia} a las {hora}"
            self.confirmacion_text.color = ft.Colors.BLUE_600
            
            # Limpiar errores
            self.limpiar_error_nombre()
            self.limpiar_error_email()
            self.limpiar_error_telefono()
            self.limpiar_error_horario()
            
            # Ocultar mensajes de éxito
            self.mensaje_exito_container.visible = False
            self.mensaje_tabla_container.visible = False
            
            # Cambiar a modo edición
            self.cambiar_modo_formulario("editar")
            
            self.page.update()
    
    def cambiar_estado_cita(self, id_cita, nuevo_estado):
        """Cambia el estado de una cita"""
        try:
            cambiar_estado_cita(id_cita, nuevo_estado)
            
            # Determinar el tipo de mensaje según el nuevo estado
            if nuevo_estado == "confirmada":
                tipo = "confirmar"
                detalle = f"Cita #{id_cita} confirmada"
            elif nuevo_estado == "cancelada":
                tipo = "cancelar"
                detalle = f"Cita #{id_cita} cancelada"
            else:
                tipo = "pendiente"
                detalle = f"Cita #{id_cita} marcada como pendiente"
            
            # Mostrar mensaje en la sección de la tabla
            self.mostrar_mensaje_exito(detalle, tipo, "tabla")
            
            # Actualizar tabla
            self.actualizar_tabla_citas()
            
        except Exception as ex:
            self.mostrar_mensaje_error(f"Error: {str(ex)}", "tabla")
    
    # ========== FUNCIONES DE UI ==========
    
    def cambiar_modo_formulario(self, modo):
        """Cambia el formulario entre modo agendar y editar"""
        if modo == "editar":
            self.boton_accion_principal.text = "ACTUALIZAR CITA"
            self.boton_accion_principal.icon = ft.Icons.UPDATE
            self.boton_cancelar.visible = True
        else:  # modo agendar
            self.boton_accion_principal.text = "AGENDAR CITA"
            self.boton_accion_principal.icon = ft.Icons.CALENDAR_MONTH
            self.boton_cancelar.visible = False
        
        self.page.update()
    
    def limpiar_formulario(self):
        """Limpia el formulario y resetea selecciones"""
        self.nombre_field.value = ""
        self.email_field.value = ""
        self.telefono_field.value = ""
        self.horario_seleccionado = None
        self.dia_seleccionado = None
        
        # Resetear botón seleccionado si existe
        if self.boton_seleccionado:
            self.boton_seleccionado.bgcolor = ft.Colors.WHITE
            self.boton_seleccionado.border = ft.border.all(1, ft.Colors.GREY_300)
            self.boton_seleccionado = None
        
        self.confirmacion_text.value = "Selecciona un horario de la tabla"
        self.confirmacion_text.color = ft.Colors.GREY_700
        
        # Limpiar errores
        self.limpiar_error_nombre()
        self.limpiar_error_email()
        self.limpiar_error_telefono()
        self.limpiar_error_horario()
        
        # No ocultar el mensaje de éxito aquí (se oculta automáticamente después de 5 segundos)
        
        self.page.update()
    
    def crear_tabla_citas(self):
        """Crea y actualiza la tabla de citas"""
        citas = obtener_citas()
        
        if not citas:
            return ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.CALENDAR_TODAY, size=40, color=ft.Colors.GREY_400),
                        ft.Text("No hay citas agendadas", size=16, color=ft.Colors.GREY_500)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                padding=30,
                bgcolor=ft.Colors.GREY_100,
                border_radius=10,
                width=900
            )
        
        # Crear encabezados de tabla
        encabezados = [
            ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Nombre", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Email", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Teléfono", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Día", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Hora", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Estado", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Acciones", weight=ft.FontWeight.BOLD)),
        ]
        
        # Crear filas de datos
        filas = []
        for cita in citas:
            id_cita, nombre, email, telefono, dia, hora, estado, fecha_creacion = cita
            
            # Determinar color del estado
            if estado == "confirmada":
                color_estado = ft.Colors.GREEN_400
                icono_estado = ft.Icons.CHECK_CIRCLE
            elif estado == "cancelada":
                color_estado = ft.Colors.RED_400
                icono_estado = ft.Icons.CANCEL
            else:
                color_estado = ft.Colors.AMBER_400
                icono_estado = ft.Icons.SCHEDULE
            
            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(id_cita))),
                        ft.DataCell(ft.Text(nombre)),
                        ft.DataCell(ft.Text(email)),
                        ft.DataCell(ft.Text(telefono)),
                        ft.DataCell(ft.Text(dia)),
                        ft.DataCell(ft.Text(hora)),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.Icon(icono_estado, size=16, color=color_estado),
                                    ft.Text(estado.upper(), size=10, color=color_estado),
                                ],
                                spacing=5
                            )
                        ),
                        ft.DataCell(
                            ft.Row(
                                [
                                    # Botón editar - SOLO para citas pendientes o confirmadas
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color=ft.Colors.BLUE_400,
                                        tooltip="Editar cita",
                                        visible=estado in ["pendiente", "confirmada"],
                                        on_click=self.crear_handler_editar(id_cita)
                                    ),
                                    # Botón confirmar (solo si está pendiente)
                                    ft.IconButton(
                                        icon=ft.Icons.CHECK_CIRCLE,
                                        icon_color=ft.Colors.GREEN_400,
                                        tooltip="Confirmar cita",
                                        visible=estado == "pendiente",
                                        on_click=self.crear_handler_confirmar(id_cita)
                                    ),
                                    # Botón marcar como pendiente (solo si está confirmada o cancelada)
                                    ft.IconButton(
                                        icon=ft.Icons.SCHEDULE,
                                        icon_color=ft.Colors.AMBER_400,
                                        tooltip="Marcar como pendiente",
                                        visible=estado in ["confirmada", "cancelada"],
                                        on_click=self.crear_handler_pendiente(id_cita)
                                    ),
                                    # Botón cancelar cita (solo si está pendiente o confirmada)
                                    ft.IconButton(
                                        icon=ft.Icons.CANCEL,
                                        icon_color=ft.Colors.RED_400,
                                        tooltip="Cancelar cita",
                                        visible=estado in ["pendiente", "confirmada"],
                                        on_click=self.crear_handler_cancelar(id_cita)
                                    )
                                ],
                                spacing=5
                            )
                        )
                    ]
                )
            )
        
        return ft.Container(
            content=ft.DataTable(
                columns=encabezados,
                rows=filas,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                horizontal_margin=10,
                column_spacing=20,
                heading_row_color=ft.Colors.AMBER_100,
                heading_row_height=50,
                data_row_max_height=60,
                data_row_color={"hovered": ft.Colors.AMBER_50},
                divider_thickness=1,
                show_bottom_border=True,
                width=900
            ),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.Colors.BLACK12),
            margin=ft.margin.only(bottom=40)
        )
    
    # ========== FUNCIONES FACTORY PARA MANEJAR CLICKS ==========
    
    def crear_handler_editar(self, id_cita):
        """Crea un handler para editar una cita específica"""
        return lambda e: self.cargar_cita_para_editar(id_cita)
    
    def crear_handler_confirmar(self, id_cita):
        """Crea un handler para confirmar una cita específica"""
        return lambda e: self.cambiar_estado_cita(id_cita, "confirmada")
    
    def crear_handler_pendiente(self, id_cita):
        """Crea un handler para marcar como pendiente una cita específica"""
        return lambda e: self.cambiar_estado_cita(id_cita, "pendiente")
    
    def crear_handler_cancelar(self, id_cita):
        """Crea un handler para cancelar una cita específica"""
        return lambda e: self.cambiar_estado_cita(id_cita, "cancelada")
    
    # ========== ACTUALIZACIÓN DE TABLA ==========
    
    def actualizar_tabla_citas(self):
        """Actualiza la tabla de citas en la interfaz"""
        # Crear nueva tabla
        nueva_tabla = self.crear_tabla_citas()
        
        # Reemplazar la tabla en la vista
        columna_principal = self.controls[0]
        
        # Buscar el índice de la tabla actual
        for i, control in enumerate(columna_principal.controls):
            if isinstance(control, ft.Container) and control == self.tabla_citas_container:
                # Reemplazar con la nueva tabla
                self.tabla_citas_container = nueva_tabla
                columna_principal.controls[i] = nueva_tabla
                break
        
        self.page.update()