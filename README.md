Proyecto de Página Web de Cámaras de Seguridad con Django
!Bienvenido a TeCuidoSecurity¡

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
Compra de Productos: Proceso de compra seguro con carrito de compras con agregar y quitar productos genera una boleta con la suma total de los productos
Tecnologías Utilizadas
Backend: Django framework para Python.
Frontend: HTML, CSS, JavaScript ,JQuery,Bootstrap.
Base de Datos: SQLite3
Seguridad: Sesiones seguras, autenticación con tokens, encriptación de contraseñas.
Instalación y Configuración
Paso a Paso
Clonar el Repositorio

git clone https://github.com/saintcarti/ProyectoEntrega3LiberonaOsses.git
cd ProyectoEntrega3LiberonaOsses/paginaWeb/

Instalar Dependencias

pip install -r requirements.txt
Configuración de la Base de Datos

python manage.py runserver
La aplicación estará disponible en http://localhost:8000.

Acceder a la Aplicación: Abrir el navegador y visitar http://localhost:8000.
Registro y Autenticación: Crear una cuenta de usuario o utilizar las credenciales del superusuario creado.
Explorar y Comprar: Navegar por el catálogo de cámaras, añadir productos al carrito y completar la compra.
Administración: Acceder al panel de administración en http://localhost:8000/admin para gestionar productos, usuarios y pedidos.
