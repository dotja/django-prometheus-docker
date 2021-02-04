from django.http import HttpResponse

def home(request):
    html = "<html><body><h1>Hello!</h1></body></html>"
    return HttpResponse(html)
