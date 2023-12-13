document.addEventListener('DOMContentLoaded', function () {
    

    if ((window.location.origin+'/') === window.location.href){
        localStorage.clear();
    } 
    if (localStorage.length === 0 && (window.location.origin+'/') !== window.location.href && (window.location.origin+'/recovery_password_vista/') !== window.location.href){
        window.location.href = window.location.origin
    }    
    // Propiedades a escuchar
    
    var acceso = document.getElementById('acceso');

    var recovery_password = document.getElementById('recovery_password');
    
    var menuR = document.getElementById('menuR');
    
    var productosR = document.getElementById('productosR');
    
    var proveedoresR = document.getElementById('proveedoresR');

    var usuariosR = document.getElementById('usuariosR');

    var comprasR = document.getElementById('comprasR');

    var ventasR = document.getElementById('ventasR');

    var analisisR = document.getElementById('analisisR');
    
    var cancelar = document.getElementById('cancelar');
    
    var realizar_compra = document.getElementById('realizar_compra');
    
    // Escuchar el evento de envío del formulario
    if (acceso !== null){
        document.getElementById('acceso').addEventListener('submit', function (event) {
        // Prevenir el envío predeterminado del formulario
        event.preventDefault();
    
        // Obtener los datos del formulario
        const formData = new FormData(event.target);
    
        // Convertir FormData a un objeto JSON (opcional)
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });
    
        // Enviar los datos a través de una solicitud HTTP (puedes usar fetch o axios)
        login('acceso' ,jsonData);
        
        });
    }
    
    // Escuchar el evento de envío del formulario
    if (recovery_password !== null){
        document.getElementById('recovery_password').addEventListener('submit', function (event) {
        // Prevenir el envío predeterminado del formulario
        event.preventDefault();
    
        // Obtener los datos del formulario
        const formData = new FormData(event.target);
    
        // Convertir FormData a un objeto JSON (opcional)
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });
    
        // Enviar los datos a través de una solicitud HTTP (puedes usar fetch o axios)
        recovery('recovery_password_vista',jsonData);
        });
    }
    
    // Escuchar el evento de envío del formulario
    if (realizar_compra !== null){
        document.getElementById('realizar_compra').addEventListener('submit', function (event) {
        // Prevenir el envío predeterminado del formulario
        event.preventDefault();
    
        // Obtener los datos del formulario
        const formData = new FormData(event.target);
    
        // Convertir FormData a un objeto JSON (opcional)
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });
    
        // Enviar los datos a través de una solicitud HTTP (puedes usar fetch o axios)
        realizar_compra_fetch('crear_compra' ,jsonData);
        
        });
    }

    if (menuR !== null){
        document.getElementById('menuR').addEventListener('click', function() {
            // Obtener datos de localStorage
            var datos = localStorage.getItem('usuario');
            document.getElementById('menuR').href = window.location.origin + '/menu/list/' + encodeURIComponent(datos);
        });
    }

    if (productosR !== null){
        document.getElementById('productosR').addEventListener('click', function() {
            // Obtener datos de localStorage
            var datos = localStorage.getItem('usuario');
            document.getElementById('productosR').href = window.location.origin + '/productos/list/' + encodeURIComponent(datos);
        });
    }

    if (proveedoresR !== null){
        document.getElementById('proveedoresR').addEventListener('click', function() {
            // Obtener datos de localStorage
            var datos = localStorage.getItem('usuario');
            document.getElementById('proveedoresR').href = window.location.origin + '/proveedores/list/' + encodeURIComponent(datos);
        });
    }

    if (usuariosR !== null){
        document.getElementById('usuariosR').addEventListener('click', function() {
            // Obtener datos de localStorage
            var datos = localStorage.getItem('usuario');
            document.getElementById('usuariosR').href = window.location.origin + '/usuarios/list/' + encodeURIComponent(datos);
        });
    }

    if (comprasR !== null){
        document.getElementById('comprasR').addEventListener('click', function() {
            // Obtener datos de localStorage
            var datos = localStorage.getItem('usuario');
            document.getElementById('comprasR').href = window.location.origin + '/compras/' + encodeURIComponent(datos);
        });
    }

    if (ventasR !== null){
        document.getElementById('ventasR').addEventListener('click', function() {
            var datos = localStorage.getItem('usuario');
            document.getElementById('ventasR').href = window.location.origin + '/ventas/' + encodeURIComponent(datos);
        });
    }

    if (analisisR !== null){
        document.getElementById('analisisR').addEventListener('click', function() {
            var datos = localStorage.getItem('usuario');
            document.getElementById('analisisR').href = window.location.origin + '/analisis/' + encodeURIComponent(datos);
        });
    }

    if (cancelar !== null){
        document.getElementById('cancelar').addEventListener('click', function() {
            window.location.href = window.location.origin ;
        });
    }
    // Función para enviar los datos a través de una solicitud HTTP
    function login(url, data) {
        fetch(`${window.location.origin}/${url}/`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            // Agregar otros encabezados según sea necesario
            },
            body: JSON.stringify(data)
        })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Error de red - ${response.status}`);
          }
          return response.json();
        })
        .then(responseData => {
            if (responseData.CODE===1){
                localStorage.setItem('usuario', JSON.parse(responseData.DATA).id);
                setTimeout(function() {
                    var datos = localStorage.getItem('usuario');
                    window.location.href = window.location.origin + '/menu/list/' + encodeURIComponent(datos);
                }, 1500);
            }
            console.log('Respuesta del servidor:', responseData);
        })
        .catch(error => {
          console.error('Error al enviar los datos:', error);
        });
    }

    // Función para enviar los datos a través de una solicitud HTTP
    function realizar_compra_fetch(url, data) {
        fetch(`${window.location.origin}/${url}/`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            // Agregar otros encabezados según sea necesario
            },
            body: JSON.stringify(data)
        })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Error de red - ${response.status}`);
          }
          return response.json();
        })
        .then(responseData => {
            if (responseData.CODE===1){
                setTimeout(function() {
                    var datos = localStorage.getItem('usuario');
                    window.location.href = window.location.origin + '/compras/' + encodeURIComponent(localStorage.getItem('usuario'));
                }, 1500);
            }
            console.log('Respuesta del servidor:', responseData);
        })
        .catch(error => {
          console.error('Error al enviar los datos:', error);
        });
    }

    function recovery(url, data) {
        fetch(`${window.location.origin}/${url}/`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            // Agregar otros encabezados según sea necesario
            },
            body: JSON.stringify(data)
        })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Error de red - ${response.status}`);
          }
          return response.json();
        })
        .then(responseData => {
            if (responseData.CODE===1){
                setTimeout(function() {
                    window.location.href = window.location.origin;
                }, 1500);
            }
            console.log('Respuesta del servidor:', responseData);
        })
        .catch(error => {
          console.error('Error al enviar los datos:', error);
        });
    }
  });