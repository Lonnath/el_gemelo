from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import json

from django.contrib.auth.models import User
from modulos.proveedores.models import Proveedor

def proveedores(request, usuario):
    banner_title = "Proveedores"
    banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    #banner_subtitle = "Nuestro Menu"
    #banner_subtexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_texto': banner_texto, 
        #'banner_subtitle': banner_subtitle, 
        #'banner_subtexto': banner_subtexto
    })
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    proveedores = Proveedor.objects.all()
    proveedores_serializados = ProveedorSerializer(proveedores, many=True)
    content = render(request, 'proveedores/list_proveedores.html', {'proveedores': proveedores_serializados.data, 'usuario': usuario})
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})



def detalle_proveedor(request, proveedor, usuario):
    
    validacion = User.objects.get(id=usuario)
    if validacion.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')

    proveedor_info = Proveedor.objects.get(id=proveedor)
    url_detalle_vendedor = '../static/img/detalle_persona.png'
    url_editar = f'../../../editar_proveedor_vista/{usuario}/{proveedor}'
    banner_title = proveedor_info.nombre
    #banner_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eius mod tempor incididunt ut labore et dolore magna."
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        #'banner_texto': banner_texto, 
    })
    detalle_proveedor = render(request, 'proveedores/detalle_proveedor.html')
    content = render(request, 'persona/detalle_persona.html', {
        'url_img': url_detalle_vendedor,
        'url_editar': url_editar,
        'detalle_proveedor': detalle_proveedor.content.decode('utf-8'),
        'usuario': usuario,
        'persona': proveedor_info,
    })
    return render(request, 'base/base.html', {
        'menu': menu.content.decode('utf-8'), 
        'banner': banner.content.decode('utf-8'), 
        'content': content.content.decode('utf-8')
    })


def editar_proveedor_vista(request, usuario, proveedor):
    
    usuario = User.objects.get(id=usuario)
    if usuario.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    proveedor_info = Proveedor.objects.get(id=proveedor)
    url_guardar = 'actualizar_proveedor'
    banner_title = "Proveedor"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title,
    })
    lista_editar = render(request, 'proveedores/editar_proveedor.html')
    content = render(request, 'persona/editar_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': '',
        'persona': proveedor_info,
        'tipo_informacion': 'PROVEEDOR'
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})


def crear_proveedor_vista(request, usuario):
    
    usuario = User.objects.get(id=usuario)
    if usuario.is_superuser:
        menu = render(request, 'base/menu_admin.html')
    else:
        menu = render(request, 'base/menu_user.html')
    url_guardar = 'crear_proveedor'
    banner_title = "Proveedor"
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title,
    })
    lista_editar = render(request, 'proveedores/crear_proveedor.html')
    content = render(request, 'persona/crear_persona.html', {
        'url_guardar': url_guardar,
        'lista_editar': lista_editar.content.decode('utf-8'),
        'campos': '',
        'tipo_informacion': 'PROVEEDOR'
    })
    return render(request, 'base/base.html', {'menu': menu.content.decode('utf-8'), 'banner': banner.content.decode('utf-8'), 'content': content.content.decode('utf-8')})

@csrf_exempt
@api_view(['POST'])
def crear_proveedor(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    proveedor = ProveedorSerializer(data=jd)
                    if proveedor.is_valid():
                        proveedor.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Creación de Proveedor Satisfactoria.'})
                    else:
                        if 'correo' in proveedor.errors:
                            raise ValidationError('Este correo ya se encuentra registrado, por favor verifique la información suministrada.')
                        else:
                            print(proveedor.errors)
                            raise ValidationError('Información invalida, verifique los datos.')
            except ValidationError as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e.detail[0])})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
def consultar_proveedores(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProveedorConsultaSerializer(data=jd)
                    if not consulta.is_valid() :
                        consulta = Proveedor.objects.all()
                    else:
                        consulta = Proveedor.objects.filter(nombre=consulta['nombre'].value)
                    proveedores = ProveedorSerializer(consulta, many=True)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": proveedores.data})
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def consultar_proveedor_editar(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    consulta = ProveedorConsultaEditarSerializer(data=jd)
                    if consulta.is_valid() :
                        consulta = Proveedor.objects.get(id=consulta['id'].value)
                    proveedores = ProveedorSerializer(consulta)
                    return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": proveedores.data})
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
            except Exception as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def editar_proveedor(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    proveedor = ProveedorConsultaEditarSerializer(data=jd)
                    if proveedor.is_valid():
                        try:
                            correo_validacion = Proveedor.objects.get(correo=proveedor['correo'].value)
                            if correo_validacion.id != proveedor['id'].value:
                                raise ValidationError('Este correo ya se encuentra registrado, por favor verifique la información suministrada.')
                        except Proveedor.DoesNotExist:
                            pass
                        proveedor_actualizar = Proveedor.objects.get(id=proveedor['id'].value)
                        proveedor_actualizar.update_proveedor(nombre=proveedor['nombre'].value, activo=proveedor['activo'].value, numero_telefono=proveedor['numero_telefono'].value, correo=proveedor['correo'].value, pais=proveedor['pais'].value, codigo_postal=proveedor['codigo_postal'].value, ciudad=proveedor['ciudad'].value, direccion=proveedor['direccion'].value)
                        proveedor_actualizar.save()
                        return Response({'CODE': 1, "MESSAGE": 'Ok.', "DATA": 'Actualizacion de Proveedor Satisfactoria.'})
                    else:
                        print(proveedor.errors)
                        raise ValidationError('Información invalida, verifique los datos.')
            except Proveedor.DoesNotExist as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": 'No se encontraron Proveedores'})
            except ValidationError as e:
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e.detail[0])})
            except Exception as e:
                print(str(e))
                return Response({'CODE': 2, "MESSAGE": 'Error.', "DATA": str(e)})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'POST':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)