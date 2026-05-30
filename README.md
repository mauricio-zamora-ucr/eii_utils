# eii_utils

Utilidades para entrada y salida en aplicaciones de consola Python.

Incluye:
- Lectura segura de enteros, flotantes, texto y booleanos.
- Lectura con validacion de rangos.
- Lecturas opcionales para flujos de edicion.
- Menus numerados reutilizables.
- Impresion de titulos decorados y mensajes con color.
- Pausa de ejecucion por ENTER.

## Instalacion

```bash
pip install eii_utilitario
```

## API publica

### Salidas

```python
from eii_utils import (
   limpiar_consola,
   generar_titulo_decorado,
   imprimir_titulo_decorado,
   imprimir_mensaje,
   imprimir_error,
   imprimir_advertencia,
   imprimir_echo,
   pausar,
)

limpiar_consola()

# Nuevo: genera contenido como string (util para archivos de texto)
titulo = generar_titulo_decorado("Sistema de ventas ACME", 60)
print(titulo)

# Compatible: sigue imprimiendo en consola
imprimir_titulo_decorado("Menu principal", 60)

imprimir_mensaje("Operacion exitosa")
imprimir_mensaje("No se pudo guardar", es_error=True)
imprimir_error("Debe ingresar un numero entero valido.")
imprimir_advertencia("El texto es obligatorio y no puede estar vacio.")
imprimir_echo("Edad", 25)

pausar()  # Muestra: Digite <ENTER> para continuar...
```

### Entradas

```python
from eii_utils import (
   leer_entero,
   leer_flotante,
   leer_texto,
   leer_booleano,
   leer_rango_enteros,
   leer_rango_flotante,
   leer_entero_opcional,
   leer_flotante_opcional,
   leer_booleano_opcional,
   leer_texto_opcional,
)

edad = leer_entero("Edad")
salario = leer_flotante("Salario")
nombre = leer_texto("Nombre", es_obligatorio=True)
activo = leer_booleano("Activo")

nota = leer_rango_enteros("Nota", 0, 100)
porcentaje = leer_rango_flotante("Porcentaje", 0.0, 100.0)

# Lecturas opcionales (si se presiona ENTER, conserva valor_actual)
edad = leer_entero_opcional("Edad", edad)
salario = leer_flotante_opcional("Salario", salario)
activo = leer_booleano_opcional("Activo", activo)
nombre = leer_texto_opcional("Nombre", nombre)
```

### Menus

```python
from eii_utils import mostrar_menu

opcion = mostrar_menu(
   titulo_menu="Menu principal",
   opciones=[
      "Agregar producto",
      "Modificar producto",
      "Eliminar producto",
      "Listar producto",
      "Ver producto",
   ],
   etiqueta_salir="Salir",  # opcion 0 (por defecto)
)

print(f"Opcion elegida: {opcion}")
```

## Ejemplo integrado

```python
from eii_utils import (
   limpiar_consola,
   imprimir_titulo_decorado,
   mostrar_menu,
   leer_texto,
   imprimir_mensaje,
   pausar,
)

while True:
   limpiar_consola()
   imprimir_titulo_decorado("Sistema de ventas ACME", 60)
   print()
   opcion = mostrar_menu(
      "Menu principal",
      [
         "Agregar producto",
         "Modificar producto",
         "Eliminar producto",
         "Listar producto",
         "Ver producto",
      ],
   )

   if opcion == 0:
      break
   if opcion == 1:
      nombre = leer_texto("Nombre del producto")
      imprimir_mensaje(f"Producto agregado: {nombre}")
   pausar()
```

## Publicar en PyPI

1. Actualiza la version en pyproject.toml.
2. Genera artefactos:

```bash
python -m pip install --upgrade build twine
python -m build
```

3. Verifica artefactos:

```bash
twine check dist/*
```

4. Sube a PyPI:

```bash
twine upload dist/*
```
