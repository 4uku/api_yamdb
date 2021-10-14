from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
import os


class SubCommand(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='filename for csv file')

    def get_current_app_path(self):
        return apps.get_app_config('reviews').path

    def get_csv_file(self, filename):
        file_path = os.path.join("static", "data", filename)
        return file_path

    def clear_model(self):
        try:
            self.model_name.objects.all().delete()
        except Exception as e:
            raise CommandError(
                f'Error in clearing {self.model_name}: {str(e)}'
            )


class GenreCategoryCommand(SubCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def insert_table_to_db(self, data):
        try:
            self.model_name.objects.create(
                name=data["name"],
                slug=data["slug"],
            )
        except Exception as e:
            raise CommandError(
                f'Error in inserting {self.model_name}: {str(e)}'
            )

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        self.stdout.write(self.style.SUCCESS(f'filename:{filename}'))
        file_path = self.get_csv_file(filename)
        line_count = 0
        model_key_fields = []
        try:
            with open(file_path, encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                self.clear_model()
                for row in csv_reader:
                    if line_count == 0:
                        model_fields = row
                    elif row != '' and line_count >= 1:
                        for i in range(1, len(row)):
                            data = {}
                            data[model_fields[i]] = row[i]
                        if data[f'{self.key_field}'] not in model_key_fields:
                            model_key_fields.append(data[f'{self.key_field}'])
                            self.insert_table_to_db(data)
                    line_count += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'{line_count} entries added to {self.model_name}'
                )
            )
        except FileNotFoundError:
            raise CommandError(f'File {file_path} does not exist')  
