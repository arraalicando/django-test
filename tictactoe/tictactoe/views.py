from django.http.response import HttpResponse


def welcome(request):
    aa = [1, 2, 3, 4]
    return HttpResponse(aa)
