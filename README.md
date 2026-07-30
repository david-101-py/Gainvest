<div align="center">
  <img src="img/Gainvest_logo.png" alt="Gainvest Logo" width="350">

  # Gainvest

  <p><b>Seguimiento personal de valores de cuentas</b><br>
  Gráficos · Tablas Excel · Reportes HTML</p>

  <p>
    <a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener">
      <img src="https://img.shields.io/github/license/david-011-py/Gainvest.py?style=flat-square&color=blue" alt="Licencia MIT">
    </a>
    <img src="https://img.shields.io/badge/Python-3.12+-blue?style=flat-square&logo=python&logoColor=white" alt="Python 3.12+">
    <a href="https://github.com/david-101-py/Gainvest/commits/" target="_blank" rel="noopener">
      <img src="https://img.shields.io/github/last-commit/david-011-py/Gainvest.py?style=flat-square&label=%C3%BAltimo%20commit" alt="Último commit">
    </a>
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square" alt="Plataformas">
  </p>
</div>

---

## Acerca de

Gainvest es una herramienta personal para llevar el registro de valores de cuentas a lo largo del tiempo. Está pensada para quien quiera visualizar la evolución de su patrimonio sin depender de servicios externos.

Todo corre localmente: los datos se almacenan en SQLite y las rutas se resuelven con `platformdirs`, siguiendo las convenciones del sistema operativo.

> **Estado actual:** El proyecto está en fase temprana. La infraestructura base está lista (carpetas, base de datos, configuración, logging), pero las funcionalidades principales están en desarrollo. Si buscas una herramienta ya funcional, vuelve más adelante.

---

## ✨ Características

<table>
  <tr>
    <th width="50%">✅ Implementado</th>
    <th width="50%">🔮 Planeado</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li>Infraestructura de carpetas multiplataforma</li>
        <li>Base de datos SQLite (3 tablas relacionales)</li>
        <li>Configuración persistente en JSON</li>
        <li>Sistema de logging en formato JSONL</li>
        <li>CRUD básico de cuentas y valores</li>
        <li>Limpieza automática de logs antiguos</li>
        <li>Limpieza de exportaciones obsoletas</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Interfaz interactiva por GUI (html-css-javascript)</li>
        <li>Generación de gráficas (matplotlib)</li>
        <li>Exportación a tablas Excel</li>
        <li>Reportes HTML autónomos</li>
        <li>Cálculos por grupos de cuentas</li>
        <li>Reasignación de cuentas entre grupos</li>
        <li>Distribución completa de la interfaz</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🏗️ Estado del proyecto

| Fase | Estado |
|---|---|
| Infraestructura (rutas, carpetas, archivos) | ✅ Completa |
| Base de datos y esquema SQLite | ✅ Completa |
| Logging y gestión de historial | ✅ Completa |
| Servicios CRUD de cuentas y grupos | 🟡 Parcial (con bugs conocidos) |
| Interfaz de terminal | ⬜ Pendiente |
| Generación de gráficos y reportes | ⬜ Pendiente |

La aplicación se puede arrancar con `python main.py`, pero actualmente no hace nada visible. El flujo real está por implementar.

---

## ⚙️ Stack

<table>
  <tr>
    <td><b>Lenguaje</b></td>
    <td>Python 3.12+</td>
  </tr>
  <tr>
    <td><b>Base de datos</b></td>
    <td>SQLite (stdlib)</td>
  </tr>
  <tr>
    <td><b>Rutas</b></td>
    <td><code>platformdirs</code> — rutas estándar del SO</td>
  </tr>
  <tr>
    <td><b>Logging</b></td>
    <td>JSONL (un archivo por día)</td>
  </tr>
  <tr>
    <td><b>Configuración</b></td>
    <td>JSON</td>
  </tr>
</table>

---

## 📁 Estructura del proyecto

<pre>
Gainvest/
├── main.py                # Punto de entrada (pendiente)
├── app/
│   └── bootstrap.py       # Inicialización al arrancar
├── core/
│   ├── folders_init.py    # Creación de carpetas base
│   ├── files_init.py      # Archivos de config y base de datos
│   ├── db_core.py         # Conexión y consultas SQLite
│   ├── config_init.py     # Lectura/escritura de configuración
│   ├── history_init.py    # Limpieza de logs antiguos
│   └── calcules.py        # (reservado) Lógica de cálculos
├── services/
│   ├── config_service.py  # Gestión interactiva de config
│   ├── data_service.py    # CRUD de cuentas, grupos y valores
│   ├── history_service.py # Sistema de logging JSONL
│   └── files_service.py   # Gestión de exportaciones
└── img/
    └── Gainvest_logo.png
</pre>

> Los datos de usuario se guardan en la carpeta de datos de la aplicación (determinada por `platformdirs`), fuera del repositorio. Las exportaciones visibles van a `Documentos/Gainvest/`.

---

## 🗄️ Esquema de base de datos

<pre>
<b>values_db</b>               # Registro de valores por cuenta
├── account_id  INTEGER   PK → accounts_metadata.id
├── value       FLOAT     NOT NULL
└── date        DATE      NOT NULL

<b>accounts_metadata</b>        # Metadatos de cuentas
├── id           INTEGER  PK AUTOINCREMENT
├── name         TEXT     NOT NULL UNIQUE
├── group_id     INTEGER  NULL → groups.group_id
├── birth_date   DATE     NOT NULL
└── total_ignore BOOLEAN  DEFAULT 0

<b>groups</b>                  # Grupos y jerarquías
├── group_id     INTEGER  PK AUTOINCREMENT
├── group_name   TEXT     NOT NULL UNIQUE
├── parent_group INTEGER  NULL → groups.group_id
└── birth_date   DATE     NOT NULL
</pre>

---

## �️ Empezar

```bash
# Clonar el repositorio
git clone https://github.com/david-011-py/Gainvest.py.git
cd Gainvest.py

# Crear y activar un entorno virtual (recomendado)
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# Instalar dependencias
pip install platformdirs

# Ejecutar
python main.py
```

Actualmente `main.py` solo carga los módulos de inicialización. No hay interfaz funcional todavía.

---

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [`LICENSE`](LICENSE) para más información.

---

<div align="center">
  <sub>Hecho por <a href="https://github.com/david-101-py">David</a> · 2026</sub>
</div>