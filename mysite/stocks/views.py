from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the stocks index.")

def stock(request, stock_number):
	return HttpResponse("You are looking at the following stock %s" % stock_number)