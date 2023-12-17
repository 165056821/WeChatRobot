import google.generativeai as genai


genai.configure(api_key=f"AIzaSyBZGNyBgy-KfheyzZEQsjoSd_H4JZSHVwE")

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("The opposite of hot is")
print(response.text)  # cold.

#
# from google.cloud import core
# from google.cloud import generative_ai
#
# proxies = {
#     "http": "http://127.0.0.1:8080",
#     "https": "http://127.0.0.1:8080",
# }
#
# channel = core.create_channel("googleapis.com", proxies=proxies)
#
# model = generative_ai.GenerativeModel("gemini-pro", channel=channel)
#
# response = model.generate_content("The opposite of hot is")

print(response.text)  # cold.
