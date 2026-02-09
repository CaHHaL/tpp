from django.http import HttpResponse
# from django.http import HttpResponseNotFound


def teacher(request):
    return HttpResponse("This is teacher_detail")

def teacher_detail(request):
    return HttpResponse("This is teacher_detail")
