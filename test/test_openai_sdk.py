import openai

openai.api_url = "https://api.openai.com"
openai.api_key = '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'

# 设置代理
openai.proxy ={"http": "127.0.0.1:50973", "https": "127.0.0.1:50973"} # 用你的代理地址替换

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response.choices[0].text.strip())
