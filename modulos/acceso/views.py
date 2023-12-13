from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render


def acceder(request):
    banner_title = "Acceso"
    banner_subtitle = ""
    banner_texto = ""
    banner_subtexto = ""
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_subtitle': banner_subtitle, 
        'banner_texto': banner_texto, 
        'banner_subtexto': banner_subtexto
    })
    
    content = render(request, 'base/login.html', {
        'url_peticion': 'acceso',
        'campo_1': 'username',
        'campo_1_texto': 'Username o email*',
        'campo_1_tipo': 'text',
        'campo_2': 'password',
        'campo_2_texto': 'Password*',
        'campo_2_tipo': 'password', 
        'boton_texto': 'INGRESAR'
    })

    return render(request, 'base/base.html', {
        'banner': banner.content.decode('utf-8'), 
        'content': content.content.decode('utf-8'),})


def recovery_password_vista(request):
    banner_title = "Recuperar Acceso"
    banner_subtitle = ""
    banner_texto = ""
    banner_subtexto = ""
    banner = render(request, 'base/banner.html', {
        'banner_title': banner_title, 
        'banner_subtitle': banner_subtitle, 
        'banner_texto': banner_texto, 
        'banner_subtexto': banner_subtexto
    })
    
    content = render(request, 'base/login.html', {'url_peticion': 'recovery_password',
        'campo_1': 'correo',
        'campo_1_texto': 'Correo de Recuperación*',
        'campo_1_tipo': 'email',
        'campo_2': 'username',
        'campo_2_texto': 'Nombre de Usuario*',
        'campo_2_tipo': 'text', 
        'boton_texto': 'RECUPERAR'
    })

    return render(request, 'base/base.html', {
        'banner': banner.content.decode('utf-8'), 
        'content': content.content.decode('utf-8'),})


@csrf_exempt
@api_view(['POST'])
def acceso(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    username = jd['username'] if 'username' in jd else None
                    password = jd['password'] if 'password' in jd else None
                    if not username or not password:
                        return Response({'CODE' : 2, 'MESSAGE' : 'ERROR', 'DATA' : 'Faltan datos.'})
                    validacion = User.objects.get(username=username)
                    bloqueos = Bloqueos.objects.get(credenciales=validacion.id)
                    if validacion and bloqueos:
                        if bloqueos.bloqueo:
                            return Response({'CODE': 4, "MESSAGE": 'CUENTA BLOQUEADA', "DATA": f'La cuenta a sido bloqueada, por favor restablezca su contraseña o comuniquese con soporte.' })
                        if check_password(password, validacion.password) :
                            bloqueos.intentos = 0
                            bloqueos.save()
                            out = {}
                            out['id'] = validacion.id
                            return Response({'CODE' : 1, 'MESSAGE' : 'ACCESO PERMITIDO', 'DATA' : json.dumps(out)})
                        else:
                            if int(bloqueos.intentos) > 1 :
                                bloqueos.bloqueo = True
                                bloqueos.save()
                                return Response({'CODE': 3, "MESSAGE": 'CONTRASEÑA INCORRECTA', "DATA": f'Intentos realizados para ingresar al portal ({bloqueos.intentos+1}), la cuenta a sido bloqueada, por favor solicite su nueva contraseña por correo o comuniquese con soporte.' })
                            bloqueos.intentos = int(bloqueos.intentos)+1
                            bloqueos.save()
                            return Response({'CODE': 3, "MESSAGE": 'CONTRASEÑA INCORRECTA', "DATA": f'Intentos restantes ({2-(int(bloqueos.intentos)-1)}) para bloquear la cuenta.'})
            except Exception as e:
                return Response({'CODE': 4, "MESSAGE": 'USUARIO NO EXISTE', "DATA": 'Verifique el Usuario de Acceso digitado.'})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view([ 'POST' ])
def crear_usuario(request):
    if request.method == 'POST':
        try:
            jd = json.loads(request.body)
            if jd:
                nombre = jd['nombre'] if 'nombre' in jd else None
                username = jd['username'] if 'username' in jd else None
                password = jd['password'] if 'password' in jd else None
                activo = jd['activo'] if 'activo' in jd else None
                correo = jd['correo'] if 'correo' in jd else None
                numero_telefono = jd['numero_telefono'] if 'numero_telefono' in jd else None
                codigo_postal = jd['codigo_postal'] if 'codigo_postal' in jd else None
                pais = jd['pais'] if 'pais' in jd else None
                direccion = jd['direccion'] if 'direccion' in jd else None
                ciudad = jd['ciudad'] if 'ciudad' in jd else None
                if not username or not password:
                    return Response({'CODE' : 2, 'MESSAGE' : 'ERROR', 'DATA' : 'Faltan datos'})
                validacion = User.objects.filter(username=username)
                if validacion:
                    return Response({'CODE': 4, "MESSAGE": "ERROR", "DATA":'Usuario ya Existe.'})
                else:
                    password_account = make_password(password)
                    usuario = User(
                        username=username, 
                        password=password_account
                    )
                    if nombre:
                        usuario.first_name = nombre
                    bloqueos = Bloqueos(credenciales=usuario)
                    empleado = Empleado(
                        usuario=usuario
                    )
                    if activo:
                        estado = True if activo == 'on' else False
                        usuario.is_active = estado
                        empleado.activo = estado
                    if correo:
                        usuario.email = correo
                        empleado.correo = correo
                    if numero_telefono:
                        empleado.numero_telefono = numero_telefono
                    if codigo_postal:
                        empleado.codigo_postal = codigo_postal
                    if pais:
                        empleado.pais = pais
                    if direccion:
                        empleado.direccion = direccion
                    if ciudad:
                        empleado.ciudad = ciudad
                    usuario.save()
                    bloqueos.save()
                    empleado.save()
                    return Response({'CODE': 1, "MESSAGE": 'REGISTRO EXITOSO', "DATA": 'Usuario Creado Exitosamente.'})
        except Exception as e:
            print(e)
            return Response({'CODE': 5, "MESSAGE": 'ACCESO DENEGADO', "DATA":''})    
@csrf_exempt
@api_view([ 'POST' ])
def recovery_password(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                if jd:
                    username = jd['username'] if 'username' in jd else None
                    if not username:
                        return Response({'CODE' : 3, 'MESSAGE' : 'ERROR', 'DATA' : 'Faltan datos'})
                    
                    validacion = User.objects.filter(username=username)
                    bloqueos = Bloqueos.objects.filter(credenciales=validacion[0].id)
                    if validacion and bloqueos:
                        validacion[0].password = make_password(validacion[0].username)
                        bloqueos[0].bloqueo = 0
                        bloqueos[0].intentos = 0
                        validacion[0].save()
                        bloqueos[0].save()
                        #MODIFICAR PARA ENVIAR PASSWORD POR CORREO
                        return Response({'CODE': 1, "MESSAGE": "Contraseña Restablecida", "DATA":f"Restablecimiento de contraseña exitoso, su contraseña es: {validacion[0].username}"})
                    else:
                        if validacion:
                            bloqueos_new = Bloqueos(credenciales=validacion[0])
                            bloqueos_new.save()
                        return Response({'CODE': 4, "MESSAGE": 'USUARIO SIN REGISTRO.', "DATA": ''})
            except Exception as e:
                print(e)
                return Response({'CODE': 3, "MESSAGE": 'USUARIO NO EXISTE', "DATA": 'Verifique el Usuario de Acceso digitado.'})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view([ 'POST' ])
def actualizar_usuario(request):
    try:
        if request.method == 'POST':
            try:
                jd = json.loads(request.body)
                
                if jd:
                    nombre = jd['nombre'] if 'nombre' in jd else None
                    username = jd['username'] if 'username' in jd else None
                    password = jd['password'] if 'password' in jd else None
                    activo = jd['activo'] if 'activo' in jd else None
                    correo = jd['correo'] if 'correo' in jd else None
                    numero_telefono = jd['numero_telefono'] if 'numero_telefono' in jd else None
                    codigo_postal = jd['codigo_postal'] if 'codigo_postal' in jd else None
                    pais = jd['pais'] if 'pais' in jd else None
                    direccion = jd['direccion'] if 'direccion' in jd else None
                    ciudad = jd['ciudad'] if 'ciudad' in jd else None
                    eliminar = True if activo == 'on' else False
                    usuario = User.objects.get(username=username)
                    usuario.username = username
                    usuario.password = password
                    usuario.is_active = eliminar
                    usuario.first_name = nombre
                    usuario.email = correo
                    empleado = Empleado.objects.get(usuario=usuario)
                    empleado.activo = eliminar
                    empleado.correo = correo
                    empleado.numero_telefono = numero_telefono
                    empleado.codigo_postal = codigo_postal
                    empleado.pais = pais
                    empleado.direccion = direccion
                    empleado.ciudad = ciudad
                    usuario.save()
                    empleado.save()
                    return Response({'CODE': 1, "MESSAGE": "Ok.", "DATA":f"Actualización realizada con exito"})
                return Response({'CODE': 2, "MESSAGE": "Error", "DATA":f"No se encontro información correcta."})    
            except Exception as e:
                print(str(e))
                return Response({'CODE': 2, "MESSAGE": 'USUARIO NO EXISTE', "DATA": 'Verifique el Usuario digitado.'})
        if request.method == 'GET':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            return Response({'CODE': 3, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'CODE': 500, "MESSAGE": 'ERROR DE METODO', "DATA":''}, status=status.HTTP_400_BAD_REQUEST)