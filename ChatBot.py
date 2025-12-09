import requests as req
from google.generativeai import GenerativeModel
import google.generativeai as gen
from dotenv import load_dotenv
import os


load_dotenv()

model = gen.GenerativeModel("gemini-2.5-flash")
API_KEY = os.getenv("GEMINI_API_KEY")
gen.configure(api_key=API_KEY)

finish = 0

if finish == 0:
    while True:
        user_input = input("How can I help you? if you finish write exit: ").lower()

        if user_input == "exit":
            finish = 1  
            print("Good Bey!!!")
            break

        else:
            model_res = model.generate_content(user_input)
            answer = model_res.candidates[0].content.parts[0].text
            print(f"--------------------------------------------\n{answer}\n--------------------------------------------")