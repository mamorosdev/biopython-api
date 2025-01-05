# FastAPI - REST

Aquest projecte forma part de l'activitat [FastAPI - Rest](https://xtec.dev/python/fastapi/rest/).

Pots baixar el projecte i treballar amb ell:

```sh
$ poetry install
$ poetry run fastapi dev app/main.py
```

Obre un navegador a <http://localhost:8000>

## Docker

Pots executar l'aplicació amb Docker:

```sh
$ docker run --rm -d --name rest -p 80:80 registry.gitlab.com/xtec/python/fastapi-rest
```

Obre el navegador a <http://0.0.0.0:80/docs>.

## Development

```sh
$ docker build --tag fastapi-rest .
$ docker run --rm --name rest -p 80:80 fastapi-rest
```

Si debug:

```sh
$ docker run --rm -it fastapi-rest /bin/sh
```