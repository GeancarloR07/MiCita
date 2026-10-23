# MiCita

Aplicación web de gestión de citas para múltiples negocios.

## Objetivo

Permitir que diferentes negocios gestionen sus servicios, profesionales,
horarios, clientes y citas desde una plataforma común, manteniendo separados
los datos de cada negocio.

Cada usuario podrá pertenecer a uno o varios negocios, con un rol y un estado
de acceso independientes para cada pertenencia.

## Tecnologías

### Backend
- Python
- FastAPI
- Pydantic
- SQLAlchemy 2.x
- Alembic
- PostgreSQL

### Frontend
- React
- TypeScript
- Vite

### Calidad y herramientas
- Git
- GitHub
- pytest
- Pruebas de frontend

## Estructura del proyecto

- `backend/`: API y lógica del servidor.
- `frontend/`: interfaz web.
- `.env.example`: plantilla de configuración.
- `.gitignore`: archivos excluidos del control de versiones.
- `alembic.ini`: configuración de las migraciones de base de datos.
- `pytest.ini`: configuración de las pruebas automatizadas.

## Estado actual

- Entorno de desarrollo configurado.
- API inicial creada con FastAPI.
- Modelos de negocios, usuarios y pertenencias implementados.
- Migraciones de base de datos configuradas con Alembic.
- Pruebas automatizadas de las reglas de pertenencia implementadas.

## Arquitectura multiempresa

MiCita está diseñada para que un mismo usuario pueda pertenecer a diferentes
negocios sin compartir automáticamente los permisos entre ellos.

Los roles contemplados son:
- `owner`: propietario.
- `admin`: administrador.
- `receptionist`: recepcionista.
- `professional`: profesional.

Las pertenencias pueden estar pendientes, activas o suspendidas. El acceso a
cada negocio deberá validarse según la pertenencia y sus permisos.

## Seguridad

- No guardar contraseñas, claves privadas ni credenciales reales en el
  repositorio.
- Utilizar variables de entorno para la configuración sensible.
- Mantener `.env` fuera del control de versiones.
- Validar la pertenencia y los permisos antes de permitir el acceso a los
  datos de un negocio.

## Desarrollo local

La configuración local se define mediante el archivo `.env`, tomando
`.env.example` como plantilla. Las dependencias de Python se instalan en un
entorno virtual.

Las migraciones de la base de datos se gestionan con Alembic y las pruebas
automatizadas se ejecutan con pytest.