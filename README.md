Proyecto de Página Web de Cámaras de Seguridad con Django
¡Bienvenido al README del proyecto de la página web de cámaras de seguridad basado en Django! Este proyecto es una plataforma de comercio electrónico diseñada para la venta de cámaras de seguridad. A continuación, detallamos las características y funcionalidades implementadas:

Funcionalidades Principales
Autenticación y Autorización
Login y Registro: Usuarios pueden registrarse y autenticarse para acceder a sus cuentas.
Roles de Usuario: Separación de roles entre administradores y clientes.
Carrito de Compras
Gestión de Carrito: Clientes pueden añadir productos al carrito, modificar cantidades y eliminar productos.
Administración de la Página
Panel de Administración: Funcionalidades administrativas para gestionar productos, usuarios y pedidos.
Gestión de Productos: CRUD (Crear, Leer, Actualizar, Eliminar) de productos.
Gestión de Usuarios: Visualización y gestión de usuarios registrados.
Gestión de Pedidos: Visualización y gestión de pedidos realizados por los clientes.
Área de Cliente
Catálogo de Productos: Clientes pueden navegar por el catálogo de cámaras de seguridad disponibles.
Compra de Productos: Proceso de compra seguro con carrito de compras y opciones de pago.
Tecnologías Utilizadas
Backend: Django framework para Python.
Frontend: HTML, CSS, JavaScript (integrados con Django templates o utilizando frameworks como React, Angular, etc.).
Base de Datos: PostgreSQL, MySQL u otra base de datos relacional compatible con Django.
Seguridad: Sesiones seguras, autenticación con tokens, encriptación de contraseñas.
Instalación y Configuración
Paso a Paso
Clonar el Repositorio

bash
Copiar código
git clone <URL_DEL_REPOSITORIO>
cd nombre_del_proyecto/
Instalar Dependencias

bash
Copiar código
pip install -r requirements.txt
Configuración de la Base de Datos

Crear una base de datos en PostgreSQL o MySQL.
Configurar la conexión en settings.py:
python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_base_de_datos',
        'USER': 'usuario_de_la_base_de_datos',
        'PASSWORD': 'contraseña_de_la_base_de_datos',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Aplicar Migraciones

bash
Copiar código
python manage.py migrate
Crear Superusuario

bash
Copiar código
python manage.py createsuperuser
Sigue las instrucciones para ingresar el nombre de usuario, correo electrónico y contraseña del administrador.
Cargar Datos Iniciales

bash
Copiar código
python manage.py loaddata datos_iniciales.json
Donde datos_iniciales.json es un archivo con datos de ejemplo para productos, usuarios u otros modelos necesarios.
Ejecutar el Servidor de Desarrollo

bash
Copiar código
python manage.py runserver
La aplicación estará disponible en http://localhost:8000.
Uso
Acceder a la Aplicación: Abrir el navegador y visitar http://localhost:8000.
Registro y Autenticación: Crear una cuenta de usuario o utilizar las credenciales del superusuario creado.
Explorar y Comprar: Navegar por el catálogo de cámaras, añadir productos al carrito y completar la compra.
Administración: Acceder al panel de administración en http://localhost:8000/admin para gestionar productos, usuarios y pedidos.
