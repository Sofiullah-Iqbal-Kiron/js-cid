# this module takes care of finding and printing solutions using googles gemini api

import google.generativeai as genai
from rich.markdown import Markdown
from rich.console import Console


# configuration
API_KEY = "AIzaSyDCn5wqFCbrdmw2Io2NlKTjLX7AZ7P9wlM"
MODEL_NAME = "gemini-1.5-flash"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
console = Console()


def geminiSolution(code: str, command: str):
    response = model.generate_content(command + "Code: " + code)
    print("")
    markdown = Markdown(response.text)
    console.print(markdown)
