from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Student


class StudentResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'name': 'first_name',
    })

    def detail(self, pk):
        return Student.objects.get(pk=pk)
