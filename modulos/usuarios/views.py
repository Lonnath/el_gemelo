from django.shortcuts import render
from django.contrib.auth.models import User
from modulos.acceso.models import Empleado

def usuarios(request, usuario):
    banner_title = "Usuarios"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    empleados_info = Empleado.objects.all()
    content = render(request, 'usuarios/list_person.html', {'usuarios': empleados_info, 'usuario': usuario})
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})



def detalle_usuario(request, usuario, empleado):
    
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    empleado_info = Empleado.objects.get(id=empleado)
    url_detalle_vendedor = '../static/img/detalle_usuario.png'
    url_editar = f'../../../editar_usuario/{usuario}/{empleado}'
    banner_title = f'{empleado_info.usuario.first_name} {empleado_info.usuario.last_name}'
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    empleado_info.activo = empleado_info.usuario.is_active
    content = render(request, 'persona/detalle_persona.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': '',
        'persona': empleado_info
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def editar_usuario(request, usuario, empleado):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    empleado_info = Empleado.objects.get(id=empleado)
    url_guardar = 'actualizar_usuario'
    banner_title = "Usuarios"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    lista_editar = render(request, 'usuarios/editar_usuario.html')
    campos = render(request, 'usuarios/editar_usuario_1.html', {
        'username': empleado_info.usuario.username,
        'password': empleado_info.usuario.password
    })
    content = render(request, 'persona/editar_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': campos.content.decode('utf-8'),
        'persona': empleado_info,
        'tipo_informacion': 'EMPLEADO',   
        'nombre': empleado_info.usuario.first_name
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def crear_usuario(request, usuario):
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    url_guardar = 'crear_usuario'
    banner_title = "Usuarios"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
    })
    lista_editar = render(request, 'usuarios/crear_usuario.html')
    campos = render(request, 'usuarios/editar_usuario_1.html', {
    })
    content = render(request, 'persona/crear_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': campos.content.decode('utf-8'),
        'tipo_informacion': 'EMPLEADO',   
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})