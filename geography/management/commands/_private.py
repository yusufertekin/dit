import re
import requests
import dateutil.parser

from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone

from geography.models import TaskInfo


class GeoBaseCommand(BaseCommand):
    help = "Import Geo Model Base Command"
    model = None
    name = None
    request_url = None

    def handle(self, task_info=None, page_size=100, page_index=None, *args, **options):
        request_url = "{}?page-size={}".format(self.request_url, page_size)
        if page_index:
            request_url = "{}&page-index={}".format(request_url, page_index)

        response = requests.get(request_url)
        now = timezone.now()
        if not task_info:
            try:
                task_info = TaskInfo.objects.get(name=self.name)
            except TaskInfo.DoesNotExist:
                task_info = TaskInfo.objects.create(name=self.name)

        self.fetch_and_save_from_response(response, task_info)
        if 'Link' in response.headers:
            new_page_index = re.search('page-index=(.+?)(&|>)', response.headers['Link']).group(1)
            if not page_index or int(page_index) < int(new_page_index):
                self.handle(task_info, page_size, new_page_index)

        task_info.latest_execution_time = now
        task_info.save()

    def fetch_and_save_from_response(self, response, task_info):
        for item in response.json().items():
            if (task_info.latest_execution_time and
                    task_info.latest_execution_time > dateutil.parser.parse(item[1]['entry-timestamp'])):
                continue

            new_instance_dict = item[1]['item'][0]
            try:
                instance = self.model.objects.get(pk=new_instance_dict[self.model.__name__.lower()])
            except self.model.DoesNotExist:
                instance = self.model()
            for field in self.model._meta.get_fields():
                field_api_name = field.name.replace('_', '-')
                if field_api_name in new_instance_dict:
                    setattr(instance, field.name, new_instance_dict[field_api_name])
            instance.save()
            print('Saving {} - {}'.format(self.model.__name__, instance.pk))
