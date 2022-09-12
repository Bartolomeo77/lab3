from django.urls import path
from . import views

app_name='encuesta'

urlpatterns = [
    path('', views.index,name='index'),
    
    path('<int:pregunta_id>/',views.detalle,name='detalle'),
    path('<int:pregunta_id>/votar',views.votar,name='votar'),

    
    
    
    path('enviar',views.enviar,name='enviar'),
    path('eje1',views.eje1,name='eje1'),
    path('eje2',views.eje2,name='eje2'),
]
