
from fastapi import FastAPI
from starlette.responses import HTMLResponse

# Load the .env file
from dotenv import load_dotenv
load_dotenv(override=True)


import os
CHATWOOT_URL = os.getenv("CHATWOOT_URL", "http://0.0.0.0:3000")
print(f"CHATWOOT_URL at '{CHATWOOT_URL}'")

CHATWOOT_WEBSITE_TOKEN = os.getenv(
    "CHATWOOT_WEBSITE_TOKEN", "JYvaTkmnKxmwWpJagk3czM1e")



from webhook import handle_event


app = FastAPI()

@app.post("/api")
async def webhook_api(event: dict):
    # print(f"Received event: {event}")
    handle_event(event)
    return event


INDEX_HTML='''<script>
  (function(d,t) {
    var BASE_URL="'''
INDEX_HTML+=CHATWOOT_URL
INDEX_HTML+='''";
    var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    g.src=BASE_URL+"/packs/js/sdk.js";
    g.defer = true;
    g.async = true;
    s.parentNode.insertBefore(g,s);
    g.onload=function(){
      window.chatwootSDK.run({
        websiteToken: "'''
INDEX_HTML+=CHATWOOT_WEBSITE_TOKEN
INDEX_HTML+='''",
        baseUrl: BASE_URL
      })
    }
  })(document,"script");
</script>'''

@app.get("/")
async def send_index_html():
    return HTMLResponse(INDEX_HTML)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
