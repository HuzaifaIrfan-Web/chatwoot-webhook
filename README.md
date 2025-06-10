# chatwoot-webhook



## Run Dev
```sh
uv run fastapi dev --host 0.0.0.0 --port 8000
```

## Run Prod
```sh
uv run fastapi run --host 0.0.0.0 --port 8000
```

```sh
uv run gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 main:app
```


## Run Docker
```sh
docker compose up --build
```