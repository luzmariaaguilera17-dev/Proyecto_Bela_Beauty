import flet as ft
import json, os
from views.navbar import NavBar

DATA_FILE = "data/reservas.json"

class HorariosView(ft.View):
    def _init_(self, page: ft.Page):
        super()._init_("/horarios", controls=[])
        self.page = page
        self.build_view()

    def build_view(self):
        # Campos de formulario
        nombre = ft.TextField(label="Nombre", width=320)
        telefono = ft.TextField(label="Teléfono", width=320)
        servicio = ft.Dropdown(
            label="Servicio", width=320,
            options=[ft.dropdown.Option(s) for s in [
                "Manicura simple",
                "Acrílico completo",
                "Esmaltado semipermanente",
                "Decoración / Nail art"
            ]]
        )
        fecha = ft.TextField(label="Fecha (dd/mm/aaaa)", width=320)
        hora = ft.TextField(label="Hora (hh:mm)", width=320)

        # Función para guardar la reserva
        def guardar_reserva(e):
            if not all([nombre.value, telefono.value, servicio.value, fecha.value, hora.value]):
                self.page.snack_bar = ft.SnackBar(ft.Text("Por favor completa todos los campos."), open=True)
                self.page.update()
                return

            reserva = {
                "nombre": nombre.value,
                "telefono": telefono.value,
                "servicio": servicio.value,
                "fecha": fecha.value,
                "hora": hora.value
            }