from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Verifica a conexão com o banco de dados'

    def handle(self, *args, **kwargs):
        db_conn = connections['default']
        try:
            # Testa a conexão com o banco de dados
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS('Banco de dados conectado com sucesso'))
        except OperationalError:
            self.stdout.write(self.style.ERROR('Não foi possível conectar ao banco de dados'))
