# chatwoot-webhook
**`Chatwoot Webhook Kafka Bridge`**

- https://github.com/HuzaifaIrfan-Infrastructure/traefik-dev
- https://github.com/HuzaifaIrfan-Platform/chatwoot-dev
- https://github.com/HuzaifaIrfan-Infrastructure/kafka-dev
- https://github.com/HuzaifaIrfan-AI/chatwoot-bot

<!-- •[Link](#)

<hr>

## 🎬 Demo Video

[![Demo](https://img.youtube.com/vi/video_id/0.jpg)](https://www.youtube.com/watch?v=video_id)

![overview](overview.drawio.png)

-->

# 🚀 Usage

## Goto Chatwoot SuperAdmin Console
- http://0.0.0.0:3000/super_admin/
- Create Agent Bot
- Set Outgoing URL as
```txt
http://your_host_ip:8000/api
```
- Copy Access Token as API Token
- Goto Inbox and set Bot Config
- In Config Copy Website Token from Messenger Script

## Create .env
```sh
cp .env.example .env
```

## Configuration
- Edit .env with your configuration


## Run Docker
```sh
docker compose up --build
```

# 🛠️ Development

## Test
```sh
uv run pytest
```


## Run Dev
```sh
uv run fastapi dev --host 0.0.0.0 --port 8000
```

## Run Prod

```sh
uv run gunicorn -c gunicorn_config.py main:app
```


# 📚 References
- https://developers.chatwoot.com/api-reference/introduction


# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)
