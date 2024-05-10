from django.contrib import admin
from django.urls import path
from inventario import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
    path('entrada/', views.entrada_inventario, name='entrada_inventario'),
    path('salida/', views.salida_inventario, name='salida_inventario'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
