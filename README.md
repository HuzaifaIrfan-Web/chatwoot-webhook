# chatwoot-webhook

## Run Dev
```sh
uv run fastapi dev --host 0.0.0.0 --port 8000
```

## Run Prod

```sh
uv run gunicorn -c gunicorn_config.py main:app
```

## Test
```sh
uv run pytest
```

## Run Docker
```sh
docker compose up --build
```