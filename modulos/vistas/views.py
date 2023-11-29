from django.shortcuts import render
import os
from configuracion.settings import BASE_DIR
from html import unescape
def index(request):
    with open(os.path.join(BASE_DIR, 'templates/menu_admin.html'), 'r') as file:
        menu = unescape(file.read())
    banner_title = "Menu"
    banner_subtitle = "Nuestro Menu"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_subtitle': banner_subtitle, 
        'banner_texto': banner_texto, 
        'banner_subtexto': banner_subtexto
    })
    content = render(request, 'menu_content.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def menu(request):
    banner_title = "Menu"
    banner_subtitle = "Nuestro Menu"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_subtitle': banner_subtitle, 
        'banner_texto': banner_texto, 
        'banner_subtexto': banner_subtexto
    })
    usuario = 2
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'menu_content.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def productos(request):
    banner_title = "Productos"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'list_productos.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def proveedores(request):
    banner_title = "Proveedores"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'list_person.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def usuarios(request):
    banner_title = "Usuarios"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'list_person_1.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def compras(request):
    banner_title = "Compras"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'list_compra.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def ventas(request):
    banner_title = "VENTAS"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'list_ventas.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def analisis(request):
    banner_title = "Analisis"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'menu_content.html')
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def detalle_producto(request):
    url_detalle_vendedor = '../static/img/detalle_persona.png'
    url_editar = '../editar_proveedor/'
    banner_title = "Hamburguesa Sencilla"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    detalle_proveedor = render(request, 'detalle_proveedor.html')
    content = render(request, 'detalle_producto.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': detalle_proveedor.content.decode('utf-8')
    })
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def detalle_proveedor(request):
    url_detalle_vendedor = '../static/img/detalle_persona.png'
    url_editar = '../editar_proveedor/'
    banner_title = "Angela White"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    detalle_proveedor = render(request, 'detalle_proveedor.html')
    content = render(request, 'detalle_persona.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': detalle_proveedor.content.decode('utf-8')
    })
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def detalle_usuario(request):
    url_detalle_vendedor = '../static/img/detalle_usuario.png'
    url_editar = '../editar_usuario/'
    banner_title = "Daniela Josefa"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    content = render(request, 'detalle_persona.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': ''
    })
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def editar_proveedor(request):
    url_guardar = '../detalle_proveedor/'
    banner_title = "Proveedor"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    lista_editar = render(request, 'editar_proveedor.html')
    content = render(request, 'editar_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': ''
    })
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

def editar_usuario(request):
    url_guardar = '../detalle_usuario/'
    banner_title = "Usuarios"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    usuario = 1
    if usuario == 1:
        menu = render(request, 'menu_admin.html')
    else:
        menu = render(request, 'menu_user.html')
    lista_editar = render(request, 'editar_usuario.html')
    campos = render(request, 'editar_usuario_1.html')
    content = render(request, 'editar_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': campos.content.decode('utf-8')
    })
    return render(request, 'base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})