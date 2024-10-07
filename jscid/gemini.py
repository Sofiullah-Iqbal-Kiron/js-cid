# this module takes care of finding and printing solutions using googles gemini api

import google.generativeai as genai
from rich.markdown import Markdown
from rich.console import Console
from dotenv import load_dotenv

from .utils import get_code


# configuration
load_dotenv()
API_KEY = "AIzaSyDCn5wqFCbrdmw2Io2NlKTjLX7AZ7P9wlM"
MODEL_NAME = "gemini-1.5-flash"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
console = Console()


def geminiSolution(file_path: str) -> None:
    code = get_code(file_path)
    response = model.generate_content(f"Check out this javascript code, if any error occurs then give some possible solutions. Code:- {code}")
    print("")
    markdown = Markdown(response.text)
    console.print(markdown)
