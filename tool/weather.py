from robot import Robot


async def weather_report(robot: Robot) -> None:
    """模拟发送天气预报
    """

    # 获取接收人
    # receivers = ["filehelper"]
    receivers = ["19372637189@chatroom"]
    # 获取天气，需要自己实现，可以参考 https://gitee.com/lch0821/WeatherScrapy 获取天气。
    report = "这就是获取到的天气情况了"

    for r in receivers:
        robot.sendTextMsg(report, r)
        # robot.sendTextMsg(report, r, "notify@all")   # 发送消息并@所有人
