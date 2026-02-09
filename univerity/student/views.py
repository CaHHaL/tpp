# Create your views here.
from django.http import HttpResponse
# from django.http import HttpResponseNotFound

def student(request):
    return HttpResponse("This is student_detail1")
def student_detail(request):
    return HttpResponse("This is student_detail")
