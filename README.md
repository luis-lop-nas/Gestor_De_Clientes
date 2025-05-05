# Gestor_De_Clientes

https://github.com/luis-lop-nas/Gestor_De_Clientes.git

# Gestor de Clientes

Este es un proyecto desarrollado en Python que permite la gestión de clientes de manera sencilla a través de una interfaz de línea de comandos (CLI) y una interfaz gráfica de usuario (GUI) basada en Tkinter.

Repositorio original: [Gestor_De_Clientes en GitHub](https://github.com/luis-lop-nas/Gestor_De_Clientes.git)

---

## Estructura del Proyecto y Funcionamiento

El proyecto está organizado para separar claramente las diferentes responsabilidades:

```
gestor_clientes/
│
├── clientes.csv
│   Archivo que almacena todos los clientes de forma persistente. Cada línea contiene un cliente en formato: DNI;Nombre;Apellido.
│
├── main.py
│   Punto de entrada del programa. Simplemente llama a `run.py` para arrancar la aplicación, permitiendo mantener un flujo limpio.
│
├── run.py
│   Decide si lanzar la versión de terminal (-t) o la versión gráfica (GUI) usando los módulos correspondientes.
│
├── gestor/ 
│   Carpeta principal que contiene toda la lógica del programa:
│
│   ├── __init__.py
│   │   Archivo vacío para indicar que `gestor` es un paquete de Python.
│   │
│   ├── menu.py
│   │   Implementa el menú de texto interactivo para trabajar desde la terminal. Permite listar, buscar, añadir, modificar y borrar clientes.
│   │
│   ├── database.py
│   │   Contiene las clases `Cliente` y `Clientes`.
│   │   - `Cliente`: representa a un cliente individual.
│   │   - `Clientes`: gestiona una lista de clientes y las operaciones de búsqueda, creación, modificación y borrado.
│   │   - Se conecta al archivo `clientes.csv` para cargar y guardar clientes de forma automática.
│   │
│   ├── helpers.py
│   │   Funciones auxiliares como validaciones de DNI, lectura de datos con control de errores y limpieza de pantalla.
│   │
│   ├── config.py
│   │   Define rutas de archivos importantes. Permite cambiar entre base de datos real y de prueba de forma automática al correr tests.
│   │
│   └── ui.py
│       Implementa la interfaz gráfica de usuario utilizando Tkinter.
│       - Muestra los clientes en una tabla (Treeview).
│       - Permite añadir, modificar o borrar clientes mediante ventanas de diálogo.
│
├── tests/
│   Carpeta que contiene pruebas automáticas para validar la funcionalidad.
│
│   ├── __init__.py
│   │   Archivo vacío para declarar la carpeta como un paquete.
│   │
│   ├── test_database.py
│   │   Pruebas unitarias sobre las operaciones principales de la clase `Clientes` (buscar, crear, modificar, borrar).
│   │
│   └── clientes_test.csv
│       Archivo CSV separado utilizado durante los tests para no alterar los datos reales de clientes.
│
├── README.md
│   Este documento. Explica cómo usar, instalar y comprender el proyecto.
│
└── requirements.txt
    Archivo que contiene las dependencias necesarias para ejecutar el proyecto (por ejemplo, pytest para testing).
```

---

## Funcionamiento General

Cuando ejecutas el programa:

- **Modo Terminal (CLI):**  
  Si ejecutas `python3 main.py -t`, se lanza un menú de texto donde puedes interactuar con los clientes.  
  Todas las operaciones sobre clientes (listar, buscar, añadir, modificar, borrar) se hacen a través del menú.

- **Modo Gráfico (GUI):**  
  Si ejecutas `python3 main.py`, se abre una ventana gráfica basada en Tkinter.  
  Puedes ver los clientes, añadir nuevos, editar datos o eliminar clientes directamente desde botones y formularios.

- **Persistencia:**  
  Todos los cambios que realices (tanto desde terminal como desde GUI) se guardan inmediatamente en `clientes.csv`, garantizando que no se pierda información.

- **Testing:**  
  Los tests automáticos aseguran que las funcionalidades básicas estén siempre funcionando correctamente, utilizando una base de datos de prueba separada.

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/luis-lop-nas/Gestor_De_Clientes.git
cd Gestor_De_Clientes
```

2. Crea y activa un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate   # En Mac o Linux
```

3. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## Uso

### Lanzar en modo terminal (CLI)

```bash
python3 main.py -t
```

### Lanzar en modo interfaz gráfica (GUI)

```bash
python3 main.py
```

---

## Testing

Este proyecto incluye tests unitarios para validar la correcta gestión de clientes.

Para ejecutar los tests:

```bash
pytest -v
```

---

## Tecnologías utilizadas

- Python 3
- Tkinter (GUI)
- Pytest (testing)

---

## Créditos

Desarrollado por Luis López como parte de un proyecto académico de programación orientada a objetos en Python.

---

¡Gracias por visitar este proyecto! 🚀