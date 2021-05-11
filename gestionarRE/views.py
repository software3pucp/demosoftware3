from django.shortcuts import render,redirect

# Create your views here.


def listarRE(request):

    context = {
    }
    return render(request,'gestionarRE/listarRE.html',context)


def editarRE(request):
    if request.POST:
        #Candidate.objects.create(name=request.POST["name"], partido=request.POST["partido"])
        print(request.POST)
        return redirect(listarRE)
    return render(request,'gestionarRE/editarRE.html')


def eliminarRE(request,pk):

    #Candidate.objects.filter(pk=pk).delete()
    print(request.POST)
    return redirect(listarRE)