# chatwoot-webhook
**`Chatwoot Webhook Kafka Bridge`**

<!-- •[Link](#)

<hr>

## 🎬 Demo Video

[![Demo](https://img.youtube.com/vi/video_id/0.jpg)](https://www.youtube.com/watch?v=video_id)

![overview](overview.drawio.png)

-->


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


# 📚 References
- https://developers.chatwoot.com/api-reference/introduction

# 🤝🏻 Connect with Me

[![GitHub ](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)
[![Email](https://img.shields.io/badge/Email-%23222.svg?style=for-the-badge&logo=gmail&logoColor=%23D14836)](mailto:hi@huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)
