
from django.shortcuts import render

from .models import Opcion,Pregunta

# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'encuesta/index.html',context)

def detalle(request,pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    context = {
        'pregunta':pregunta
    }
    
    return render(request,'encuesta/detalle.html',context)


def votar(request,pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    opcionSeleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    opcionSeleccionada.votos += 1
    opcionSeleccionada.save()
    context = {
        'pregunta':pregunta
    }
    return render(request,'encuesta/resultados.html',context)








def enviar(request):
    context2 = {
        'titulo':"Respuesta",
        'nombre':request.POST['nombre'],
        'clave':request.POST['password'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'correo':request.POST['email'],
        'website':request.POST['sitioweb'],
    }
    return render(request,'encuesta/respuesta.html',context2)

def eje1(request):

    if request.POST['operacion'] == 'suma':
        date1 = int(request.POST['dat1']) + int(request.POST['dat2'])
    elif request.POST['operacion'] == 'resta':
        date1 = int(request.POST['dat1']) - int(request.POST['dat2'])
    elif request.POST['operacion'] == 'multi':
        date1 = int(request.POST['dat1']) * int(request.POST['dat2'])
    context3 = {
        'operacion':request.POST['operacion'],
        'dat1':request.POST['dat1'],
        'dat2':request.POST['dat2'],
        'operacion':request.POST['operacion'],
        'dates':date1,
    }
    return render(request,'encuesta/res1.html',context3)

def eje2(request):
    dar =  (float(request.POST['dat1'])/2) 
    total = 3.14 * dar*dar * float(request.POST['dat2'])
    context4 = {
        'date':total,
    }
    return render(request,'encuesta/res2.html',context4)






# Create your views here.
