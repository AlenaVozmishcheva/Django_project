from django.core.management import BaseCommand

import pyodbc

from config.settings import USER, PASSWORD, HOST, PAD_DATABASE, DRIVER, DATABASE

class Command(BaseCommand):

    def handle(self, *args, **options):
        ConnectionString = f"""DRIVER={DRIVER};
        SERVER={HOST};
        DATABASE={PAD_DATABASE};
        UID={USER};
        PWD={PASSWORD}"""

        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
            # conn.execute(fr"DROP DATABASE {DATABASE};")
                conn.execute(fr'CREATE DATABASE {DATABASE};')
            except pyodbc.ProgrammingError as ex:
                print(ex)
            else:
                print(f'База данных {DATABASE} успешно создана')