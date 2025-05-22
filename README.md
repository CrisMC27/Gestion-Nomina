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

