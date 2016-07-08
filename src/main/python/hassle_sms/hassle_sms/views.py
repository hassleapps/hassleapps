from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


@csrf_exempt
def home(request):
    return HttpResponse(render_to_string('home.html'), content_type='text/html')

@csrf_exempt
def sms(request):
    return HttpResponse(render_to_string('sms.xml'), content_type='text/xml')
