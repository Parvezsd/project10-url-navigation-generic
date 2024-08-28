from django.shortcuts import render # type: ignore

# Create your views here.
def conditions(request):
    d={'a':100,'b':50}
    return render(request,'conditions.html',d)

def loop(request):
    d={'name':'Parvez','mob':[9652704985]}
    return render(request,'loop.html',d)