from django.http import HttpResponse


def index(request):
    # comment
    return HttpResponse('Hello')
