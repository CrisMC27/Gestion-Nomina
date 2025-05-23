#  Sistema de Gestión de Nómina - Microservicios con FastAPI + PostgreSQL

Este proyecto es un sistema de gestión de nómina desarrollado con **arquitectura de microservicios**, utilizando **FastAPI**, **PostgreSQL** y un **frontend HTML + Bootstrap**. Permite administrar empleados, novedades, cálculo de nómina y generar desprendibles en PDF.

---

##  Tecnologías Utilizadas

- **FastAPI** (backend de microservicios)
- **PostgreSQL** (base de datos)
- **HTML + Bootstrap** (frontend visual)
- **JavaScript (fetch API)** para comunicación entre microservicios
- **Uvicorn** como servidor ASGI

---

##  Arquitectura de Microservicios

El sistema se divide en servicios independientes:

| Microservicio    | Descripción |
|------------------|-------------|
| `frontend`       | Manejo de interfaces (login, empleados, formularios) |
| `empleados`      | CRUD de empleados con conexión a PostgreSQL |
| `nomina`         | (Próximamente) Cálculo automático de nómina |
| `novedades`      | (Próximamente) Incapacidades, licencias, ausencias |

Los microservicios se comunican vía **HTTP (REST)** a través de endpoints expuestos por cada uno.

---

## 📁 Estructura del Proyecto

djangoAppNomina/
├── empleados/
│ ├── main.py
│ ├── database.py
│ ├── models/
│ ├── routers/
│ └── schemas/
├── frontend/
│ ├── main.py
│ └── templates/
│ ├── login.html
│ └── empleados.html
├── requirements.txt
└── README.md


---


---


## ⚙️ Instalación y Configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tuusuario/gestion-nomina.git
   cd gestion-nomina

 # Crear entorno virtual

 python -m venv venv
venv\Scripts\activate     # En Windows

# Instalar dependencias

pip install -r requirements.txt

# Configurar la base de datos

Asegúrate de tener PostgreSQL corriendo con una base de datos llamada nomina_db.

Puedes modificar database.py con tus credenciales:

DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/nomina_db"

##  Cómo ejecutar

python -m empleados.main --reload --port 8002

## Ejecutar el frontend

python -m uvicorn frontend.main:app --reload --port 8001

##  Acceso

Frontend: http://localhost:8001/empleados

API Empleados: http://localhost:8002/docs

# Funcionalidades actuales

Registro de empleados

Edición y eliminación de empleados

Listado en tabla dinámica

Interfaz responsiva con Bootstrap

Separación de servicios por dominio

##  Pendientes / Roadmap
Cálculo de nómina automática

Desprendible de pago en PDF

Roles de usuario: empleador / empleado

Gestión de novedades (incapacidades, licencias)

Exportar a Excel y reportes contables








