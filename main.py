#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
from argparse import ArgumentParser

from configuration import Config
from constants import ChatType
from db.init import init_db
from robot import Robot, __version__
from wcferry import Wcf
import asyncio


# app = FastAPI()
#
# register_tortoise(
#     app,
#     config=config,
#     generate_schemas=True,
#     add_exception_handlers=True,
# )


async def main(chat_type: int):

   # try:
       await init_db()
       config = Config()
       wcf = Wcf(debug=True)
       def handler(sig, frame):
           wcf.cleanup()  # 退出前清理环境
           # await Log.create(message=f"软件正常退出", level="INFO", source="AiHelper")
           exit(0)

       signal.signal(signal.SIGINT, handler)

       robot = Robot(config, wcf, chat_type)
       robot.LOG.info(f"WeChatRobot【{__version__}】成功启动···")

       # 机器人启动发送测试消息
       # robot.sendTextMsg("机器人启动成功！", "filehelper")
       robot.sendTextMsg("机器人启动成功！", "39261378509@chatroom")
       # robot.sendTextMsg("机器人启动成功！", "19372637189@chatroom")
       # robot.sendTextMsg("机器人启动成功！", "38800851173@chatroom")
       # robot.sendTextMsg("机器人启动成功！", "5615633546@chatroom")
       # 5615633546@chatroom 家人群
       # 39261378509@chatroom 测试群
       # 19372637189@chatroom 信息化工作专班
       # 38800851173@chatroom 李旭东科长工作群
       # 接收消息
       # robot.enableRecvMsg()     # 可能会丢消息？
       robot.enableReceivingMsg()  # 加队列

       # # 每天 7 点发送天气预报
       # robot.onEveryTime("07:00", weather_report, robot=robot)
       #
       # # 每天 7:30 发送新闻
       # robot.onEveryTime("07:30", robot.newsReport)
       #
       # # 每天 16:30 提醒发日报周报月报
       # robot.onEveryTime("16:30", ReportReminder.remind, robot=robot)

       # 让机器人一直跑
       robot.keepRunningAndBlockProcess()
    # except Exception as e:
    #     # 记录异常
    #     await Log.create(message=f"Exiting due to exception: {e}", level="INFO", source="AiHelper")
    # else:
    #     # 记录正常退出
    #     await Log.create(message=f"Exiting normally", level="INFO", source="AiHelper")

# templates = Jinja2Templates(directory="templates")
#
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "message": "欢迎来到我的 FastAPI test 应用！"})


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-c', type=int, default=3, help=f'选择模型参数序号: {ChatType.help_hint()}')
    args = parser.parse_args().c
    asyncio.run(main(args))

# 启动应用，监听 8000 端口
# import uvicorn
# uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
