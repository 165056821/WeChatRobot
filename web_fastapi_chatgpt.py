import json
from collections import defaultdict
from typing import List
from httpx import AsyncClient
from configuration import Config
from fastapi import FastAPI, WebSocket, Response
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
config = Config()
# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)

app = FastAPI(middleware=[Middleware(CORSMiddleware, allow_origins=['*'])])

# @app.middleware("http")
# async def add_csp_header(request, call_next):
#     response = await call_next(request)
#     response.headers['Content-Security-Policy'] = "connect-src 'self' ws://192.168.10.21:8000;"
#     return response


async def request(val: List[dict[str, str]]):
    """
    发起请求
    :param val:对话内容
    :return:
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.CHATGPT["key"],
    }
    params = {
        "model": "gpt-4-1106-preview",
        "messages": val,
        "temperature": 0.8,
        "n": 1,
        "max_tokens": 3000,
        "stream": True,
    }
    # 添加代理设置

    proxies = {
        "http://": "http://127.0.0.1:50937",
        "https://": "http://127.0.0.1:50937",
    }

    async with AsyncClient(proxies=proxies) as client:
        async with client.stream("POST", url, headers=headers, json=params) as response:
            async for line in response.aiter_lines():
                if line.strip() == "":
                    continue
                line = line.replace("data:", "")
                if line.strip() == "[DONE]":
                    return
                date = json.loads(line)

                if date.get("choices") is None or len(date.get("choices")) == 0 or date.get("choices")[0].get(
                        "delta").get("finish_reason") is not None:
                    return
                yield date.get("choices")[0]


@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    message = []
    while True:
        data = await websocket.receive_text()
        if  data=="quit":
            await websocket.close()
            break
        message.append({"role": "user", "content": data})
        chat_msg = defaultdict(str)
        async for i in request(message):
            if i.get("delta").get("role"):
                chat_msg["role"] = i.get("delta").get("role")
            if i.get("delta").get("content"):
               chat_msg["content"] += i.get("delta").get("content")
               await websocket.send_text(i.get("delta").get("content"))
        message.append(chat_msg)

templates = Jinja2Templates(directory="templates")
@app.get("/html", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "欢迎来到我的 FastAPI test 应用！"})


@app.get("/vue", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("vue.html",{"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("web_fastapi_chatgpt:app", host="0.0.0.0", port=8000,
                log_level="info")


# async def chat_test(inp: str):
#     message = [{"role": "user", "content": inp}]
#     chat_msg = defaultdict(str)
#     async for i in request(message):
#         if i.get("delta").get("role"):
#             chat_msg["role"] = i.get("delta").get("role")
#         if i.get("delta").get("content"):
#             chat_msg["content"] += i.get("delta").get("content")
#
#     print(chat_msg)
#
#
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(chat_test("你好呀"))


