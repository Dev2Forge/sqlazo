# SQLAZO

> [!WARNING]
> Contiene algunos errores que pueden ser controlados con bloques `try`, revise constantemente el archivo de registros `./log.log`, allí se detallan los errores que pasé por alto.<br>
> Los corregiré en las próximas semanas...

---

<div style="display: flex; align-items: center; justify-content: center; margin: 10px 0; gap: 10px; max-height: 48px; height: 48px;">
  <a href="https://github.com/sponsors/tutosrive" target="_blank">
  <img src="https://img.shields.io/badge/Sponsor-%F0%9F%92%96%20tutosrive-orange?style=for-the-badge&logo=github" alt="Sponsor me on GitHub">
</a>
  <a href="https://www.buymeacoffee.com/tutosrive">
    <img 
      src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=tutosrive&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" 
      style="height: 48px; width: auto; object-fit: contain; border-radius: 6px;" 
      alt="Buy me a coffee button">
  </a>
</div>

---

  <!-- Badges -->
  <div>
<!-- Total downloads -->
    <a href="https://pepy.tech/projects/sqlazo"><img src="https://static.pepy.tech/badge/sqlazo" alt="PyPI Downloads"></a>
<!-- Versión actual -->
    <a href="https://pypi.org/project/sqlazo/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/sqlazo?label=sqlazo"></a>
<!-- Python versions supported -->
    <a href="https://python.org/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/sqlazo"></a> 
<!-- Author -->
    <a href="https://github.com/tutosrive"><img alt="Static Badge" src="https://img.shields.io/badge/Tutos%20Rive-Author-brightgreen"></a>
<!-- Licencia -->
    <a href="https://raw.githubusercontent.com/tutosrive/sqlazo/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/tutosrive/sqlazo"></a>
  </div>

```shell
pip install sqlazo
```
---

Es un módulo para gestionar bases de datos _SQLITE_. Le permite acceder a métodos que realizan **transacciones** con la base de datos que usted elija, siempre y cuando sea una base de datos _SQLITE_

## Inicialización

Para iniciar, su uso, se hará una instancia de la clase **Database**, la cual recibe los siguientes parámetros:

`name:str`: Nombre de la base de datos (Ej: `'test.db'`).
`check_thread:boolean`: Verificar ejecuciones multihilo.

```py
# Ejemplo de inicialización
from sqlazo import Database

db = Database('test.db', False)
# Creará un archivo test.db listo para usar...
```

## Métodos disponibles

- `create_table`: Permite crear una tabla en la base de datos conectada.
- `insert_data`: Ejecuta la "consulta" de inserción en la base de datos (Agrega datos).
- `get_data_all`: Ejecuta la "consulta" para obtener todos los registros de la base de datos.
- `get_data_where`: Ejecuta la "consulta" para obtener registros con "consulta personalizada".
- `delete_data`: Eliminar registros dea base de datos.

## Métodos privados 🔏
- `__connect`: Realizar conexión a la base de datos.
- `__commit`: "Refrescar" cambios en la base de datos.
- `__cursor`: Crea un cursor en la conexión a la base de datos, el cual permite "ejecutar consultas".

## Historial de versiones:
- `0.1.5`: Actualización de dependencias y links
- `0.1.4`: Actualización de dependencias y links
- `0.1.3`: Actualización de versiones de dependencias
- `0.1.2`: Actualización de versiones de dependencias
- `0.1.1`: Se agregó el manejo de dependencias en el archivo de construcción (.toml)
- `0.1.0`: Versión inicial

## Si desea conocer más acerca de, visite:
- [Web de soporte](https://tutosrive.github.io/sqlazo/)
- [Web pypi.org](https://pypi.org/project/sqlazo/)
- [Github project](https://github.com/Dev2Forge/sqlazo/)
