from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
  def get(self, request):
    return HttpResponse('Hello')
  
import csv

header = ['ID', '名前', '年齢']

people = [
    ('1', 'Hoge', 10),
    ('2', 'Fuga', 18),
    ('3', 'Foo', 23),
]


class CSVView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mycsv.csv"'

        writer = csv.writer(response)
        writer.writerow(header)
        writer.writerows(people)
        return response