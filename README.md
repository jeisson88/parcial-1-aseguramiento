README - Parcial 1 Aseguramiento de la Calidad
Parcial 1 - Aseguramiento de la Calidad de Software

Este proyecto es un prototipo de solución de software que cumple con los estándares de calidad solicitados en la rúbrica de evaluación:

- ✅ Clase abstracta (BaseComponent)
- ✅ Dos interfaces (Versionable, Documentable)
- ✅ Dos clases concretas (WebServiceModule, DataProcessingModule) que heredan de la clase abstracta e implementan las interfaces
- ✅ Pruebas automáticas con pytest
- ✅ Buenas prácticas: estructura modular, .gitignore, documentación y control de versiones con Git

📂 Estructura del Proyecto
PARCIAL 1 ASEGURAMIENTO/
├─ src/
│  └─ calidad/
│     ├─ __init__.py
│     ├─ base.py
│     ├─ interfaces.py
│     └─ modules.py
├─ tests/
│  └─ test_modules.py
├─ main.py
├─ pyproject.toml
├─ .gitignore
├─ README.md
└─ LICENSE

🚀 Requisitos
- Python 3.10 o superior
- pytest (para ejecutar las pruebas)
- ruff (opcional, para análisis de código y buenas prácticas)

🔧 Instalación y Ejecución

1. Clonar el repositorio
git clone https://github.com/jeisson888/parcial-1-aseguramiento.git
cd parcial-1-aseguramiento

2. Crear entorno virtual
python -m venv .venv

3. Activar entorno virtual
- Windows:
.venv\Scripts\activate
- Mac / Linux:
source .venv/bin/activate

4. Instalar dependencias
pip install pytest ruff

5. Ejecutar pruebas
pytest

6. Ejecutar programa
python main.py

🧪 Ejemplo de Salida
[2025-08-09T15:00:01] [UsuariosAPI] Validación OK
[2025-08-09T15:00:01] [ETLFacturas] Validación OK
[2025-08-09T15:00:01] [UsuariosAPI] Versión actualizada a 1.1.0
[2025-08-09T15:00:01] [ETLFacturas] Versión actualizada a 0.1.1
# UsuariosAPI
- Tipo: WebServiceModule
- Dueño: Equipo Backend
- Versión: 1.1.0
- Base URL: /api/v1/users
- Estándar: UMG-QA-1.0

# ETLFacturas
- Tipo: DataProcessingModule
- Dueño: Equipo Datos
- Versión: 0.1.1
- Batch size: 5000
- Estándar: UMG-QA-1.0

📜 Licencia
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

✨ Créditos
Proyecto desarrollado como parte del Parcial 1 de la asignatura Aseguramiento de la Calidad de Software.

