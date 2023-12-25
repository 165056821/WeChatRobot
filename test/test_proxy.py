import httpx
import asyncio

# 设置代理
# 如果是 HTTP/HTTPS 代理
proxies = {
    "http://": "http://127.0.0.1:50973",
    "https://": "http://127.0.0.1:50973",
}

# 如果是 SOCKS5 代理
# proxies = {
#     "http://": "socks5://127.0.0.1:50973",
#     "https://": "socks5://127.0.0.1:50973",
# }

# 你的 OpenAI API 信息
url = "https://api.openai.com/v1/engines"
headers = {"Authorization": "Bearer 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"}

# 发送请求的异步函数
async def fetch_openai_api():
    async with httpx.AsyncClient(proxies=proxies) as client:
        response = await client.get(url, headers=headers)
        print(response.json())

# 运行异步事件循环
if __name__ == "__main__":
    asyncio.run(fetch_openai_api())
