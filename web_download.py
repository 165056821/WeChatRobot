import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()


templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "message": "欢迎来到我的 FastAPI 应用！"})

directory_path = "./download"  # 替换为你的文件存储目录

#从文件夹中获取文件列表
files = os.listdir(directory_path)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("download.html", {"request": request, "files": files})

@app.get("/download/{file_name}")
def download_file(file_name: str):
    file_path = f'{directory_path}/{file_name}'  # 替换为你的文件实际存储路径
    return FileResponse(file_path, media_type='application/octet-stream', filename=file_name)

if __name__ == "__main__":
    # 启动应用，监听 8000 端口
    import uvicorn
    uvicorn.run("web_download:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
