import pathlib
import textwrap
import os
import google.generativeai as genai

from config.config import config

GOOGLE_API_KEY = config["GOOGLE_GEMINI_API_KEY"]


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def process_gemini(user_prompt):
    response = model.generate_content(user_prompt)
    return response.text