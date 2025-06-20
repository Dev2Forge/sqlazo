# SQLAZO

---

<div align="center" style="display: flex; align-items: center; justify-content: center; margin: 10px 0; gap: 10px; max-height: 48px; height: 48px;">
  <a href="https://github.com/sponsors/tutosrive" target="_blank">
  <img src="https://img.shields.io/badge/Sponsor-%F0%9F%92%96%20Dev2Forge-blue?style=for-the-badge&logo=github" alt="Sponsor me on GitHub">
</a>
  <a href="https://ko-fi.com/D1D61GNZR1" target="_blank">
  <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Sponsor me on Ko-Fi">
</a>
</div>

---

<!-- Badges -->

<div>
<!-- Total downloads -->
  <a href="https://pepy.tech/projects/sqlazo"><img src="https://static.pepy.tech/badge/sqlazo" alt="PyPI Downloads"></a>
<!-- Current version -->
  <a href="https://pypi.org/project/sqlazo/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/sqlazo?label=sqlazo"></a>
<!-- Supported Python versions -->
  <a href="https://python.org/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/sqlazo"></a>
<!-- Author -->
  <a href="https://github.com/tutosrive"><img alt="Static Badge" src="https://img.shields.io/badge/Tutos%20Rive-Author-brightgreen"></a>
<!-- Licence -->
  <a href="https://github.com/Dev2Forge/sqlazo/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/dev2forge/sqlazo"></a>
</div>

```shell
pip install sqlazo
```

---

It is a module for managing *SQLITE* databases. It provides access to methods that perform **transactions** with the database of your choice, as long as it is a *SQLITE* database.

## Initialisation

To begin using it, create an instance of the **Database** class, which accepts the following parameters:

`name: str`: Name of the database (e.g. `'test.db'`).
`check_thread: boolean`: Check for multithreaded executions.

```py
# Initialisation example
from sqlazo import Database

# Will create a test.db file ready to use
# check threads is False by default
db = Database('test.db')
```

## Available Methods

* `create_table`: Allows you to create a table in the connected database.
* `table_exists`: Allows you to check if a table exists in the database.
* `insert_data`: Executes the insertion "query" in the database (adds data).
* `get_data_all`: Executes the "query" to retrieve all records from the database.
* `get_data_where`: Executes the "query" to retrieve records using a "custom query".
* `delete_data`: Deletes records from the database.

## Private Methods 🔏

* `__connect`: Establishes connection to the database.
* `__commit`: "Refreshes" changes to the database.
* `__cursor`: Creates a cursor on the database connection, allowing "query execution".

## Version History:

- `0.2.0`: A new method was added to correctly check whether a table exists or not, and the code was modified to try to be
  compatible with older versions of Python and:
  - `Fix`: [issue #1](https://github.com/Dev2Forge/sqlazo/issues/1)
  - `Update`: Links and e-mail support
  - `Feat`: Added new method [`table_exists`](#available-methods)
- `0.1.5`: Updated dependencies and links
- `0.1.4`: Updated dependencies and links
- `0.1.3`: Updated dependency versions
- `0.1.2`: Updated dependency versions
- `0.1.1`: Added dependency handling in the build file (.toml)
- `0.1.0`: Initial release

## If you wish to learn more, visit:

* [Support website](https://docs.dev2forge.software/sqlazo/)
* [PyPI page](https://pypi.org/project/sqlazo/)
* [GitHub project](https://github.com/dev2forge/sqlazo/)
