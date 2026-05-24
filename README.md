# eii_utils
Módulo utilitario de Python para entrada/salida en consola.

## Instalación
```bash
pip install eii_utils
```

## Uso básico
```python
from eii_utils import (
    leer_entero,
    leer_flotante,
    leer_texto,
    leer_booleano,
    leer_rango_enteros,
    leer_rango_flotante,
    limpiar_consola,
    imprimir_titulo_decorado,
    imprimir_mensaje,
)

edad = leer_entero("Edad")
nota = leer_rango_flotante("Nota", 0.0, 100.0)
nombre = leer_texto("Nombre")
es_activo = leer_booleano("¿Activo?")

limpiar_consola()
imprimir_titulo_decorado("resultado", largo=30)
imprimir_mensaje(f"Usuario: {nombre}")
imprimir_mensaje("No se pudo guardar", es_error=True)
```

## Publicar en PyPI
1. Actualiza la versión en `pyproject.toml`.
2. Genera los artefactos:
   ```bash
   python -m pip install --upgrade build twine
   python -m build
   ```
3. Verifica los artefactos:
   ```bash
   twine check dist/*
   ```
4. Sube a PyPI:
   ```bash
   twine upload dist/*
   ```
