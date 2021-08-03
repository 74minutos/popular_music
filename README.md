
# Overview

En este repo tenemos dos procesos separados. Por un lado nos encontramos con el paquete spotidy_data, que se encarga de recoger a información que necesitamos a través de la API de spotify.



## Installation

Instalaremos todos los requirements a través de este código:

```bash
pip install -r requirements.txt
```

## Usage

En este caso he trabajado con un dataset de spotify. Para extraerlo básicamente le he pedido que me devolviera el máximo número de resultados por año (1.000), desde los años 40. Esto hace un total de 81.000 álbumes. Todo esto se realiza a través del módulo get_albums del módulo spotify_data. Esto genera un csv.

Para utilizar el paquete y que el módulo nos genere el csv que necesitamos (si no estáis a gusto con el que ya está listo en el repositorio), podéis lanzar este código:

```
env/bin/python -m spotify_data.get_albums\
  --credentials_path credentials/spotify_credentials.json
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
