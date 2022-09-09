from django .shortcuts import render
from django .shortcuts import HttpResponse

def Menu(requset):
    return render(requset,"index.html",{})

# def Punnam(request):
#     return render(request,"punnam.html",{})
#
# def Ramala(request):
#     return render(request,"ramala.html",{})