
# Overview

A través de este repositorio quiero conseguir unos datos que me permitan hacer una visualización de los géneros musicales a través de las últimas décadas.


## Instalación

1. instalamos virtualenv:
  `python3 -m venv env`
2. instalamos requirements en virtual env:
  `env/bin/pip install -r requirements.txt`
3. podemos utilizar un intérprete en el entorno virtual de esta manera:
  `env/bin/python`
4. creamos la variable de entorno para nuestras credenciales de google:
  `export GOOGLE_APPLICATION_CREDENTIALS="credentials/google_credentials.json"`

## Usage

En este caso he trabajado con un dataset de spotify. Para extraerlo básicamente le he pedido que me devolviera el máximo número de resultados por año (1.000), desde los años 40. Esto hace un total de 81.000 canciones. Todo esto se realiza a través del módulo get_tracks del módulo spotify_data. Esto genera un csv.

Para utilizar el paquete y que el módulo nos genere el csv que necesitamos (si no estáis a gusto con el que ya está listo en el repositorio), podéis lanzar este código:

```
env/bin/python -m spotify_data.get_tracks\
  --credentials_path credentials/spotify_credentials.json
```

Si quisiéramos subir esta info a BigQuery, tal y como he hecho para este proyecto, usaríamos el módulo upload_to_bigquery (cambiando los nombres de cliente, proyectos, tablas..):

```
env/bin/python -m spotify_data.upload_to_bigquery
```

## Running Tests

Para testear los posibles errores de linting en el paquete, ejecutar:

```bash
  env/bin/python -m flake8 --select F spotify_data
```

Para testear los posibles errores de typing en el paquete, ejecutar:

```bash
env/bin/python -m mypy --check-untyped-defs --ignore-missing-imports spotify_data
```
