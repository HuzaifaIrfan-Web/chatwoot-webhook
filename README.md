# chatwoot-webhook

## Goto Chatwoot SuperAdmin Console
- http://0.0.0.0:3000/super_admin/
- Create Agent Bot
- Set Outgoing URL as
```txt
http://host.docker.internal:8000/api
```
- Copy Access Token as API Token
- Goto Inbox and set Bot Config
- In Config Copy Website Token from Messenger Script

## Create .env
```sh
cp .env.example .env
```
- Use chatwoot URL or Use Correct one. 
```txt
http://host.docker.internal:3000
```

## Test
```sh
uv run pytest
```

## Run Docker
```sh
docker compose up --build
```

## Run Dev
```sh
uv run fastapi dev --host 0.0.0.0 --port 8000
```

## Run Prod

```sh
uv run gunicorn -c gunicorn_config.py main:app
```
