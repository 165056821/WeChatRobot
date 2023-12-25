from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "欢迎来到我的 FastAPI test 应用！"})


if __name__ == "__main__":
    # 启动应用，监听 8000 端口
    import uvicorn
    uvicorn.run("web_fastapi:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
