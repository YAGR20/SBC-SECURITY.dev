import csv
import os
from django.core.management.base import BaseCommand
from sbc_app.models import EventoSeguridad
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa eventos de seguridad desde un archivo CSV generado por Wazuh'

    def handle(self, *args, **options):
        # Define la ruta al archivo CSV. Asegúrate de tener el archivo en la ruta correcta.
        ruta_csv = os.path.join(settings.BASE_DIR, 'sbc_app', 'data', 'wazuh_events.csv')
        
        if not os.path.exists(ruta_csv):
            self.stdout.write(self.style.ERROR(f"No se encontró el archivo: {ruta_csv}"))
            return

        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                try:
                    # Si el formato de fecha no es directamente compatible, usa datetime.strptime
                    fecha = datetime.strptime(fila['fecha'], "%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al procesar la fecha en la fila: {fila['fecha']}. Error: {e}"))
                    continue

                EventoSeguridad.objects.create(
                    fecha=fecha,
                    ip=fila['ip'],
                    tipo_ataque=fila['tipo_ataque'],
                    descripcion=fila['descripcion']
                )
        self.stdout.write(self.style.SUCCESS("Importación de CSV completada correctamente."))
