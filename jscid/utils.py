import sys
import time # sleep and other time utility
from typing import Set
from collections import namedtuple
import json

# rich
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax


SINGLE_QUOTE = "'"
DOUBLE_QUOTE = '"'
SINGLE_SPACE = " "
EMPTY_STRING = ""
COMMA = ","

# StackOverFlow API
API_VERSION = 2.3
BASE_URL = f"https://api.stackexchange.com/{API_VERSION}"
SEARCH_URL = BASE_URL + f"/search?site=stackoverflow"
ANSWERS_URL = BASE_URL + f"/questions/<id>/answers?site=stackoverflow" + "&filter=withbody" + "&order=desc" + "&sort=votes"

error_types = {
    "TypeError": "TypeError",
    "RangeError": "RangeError",
    "ReferenceError": "ReferenceError",
    "SyntaxError": "ReferenceError",
    "InternalError": "InternalError",
    "URIError": "URIError",
    "EvalError": "EvalError",
}

Question = namedtuple("Question", ["id", "has_accepted"])
Answer = namedtuple("Answer", ["id", "accepted", "score", "body", "author"])

HINT_MESSAGES = {
    "TypeError": "Unsupported data type or unusual operation.",
    "ReferenceError": "Variable reference can't be found, may be not declared.",
    "InternalError": "Too much data so call stack exceeds it's critical size",
    "SyntaxError": "You have a syntax error somewhere around line",
    "URIError": "Wrong characters are used in URI function",
}

console = Console()


def check_availability(file_path: str) -> None:
    try:
        with open(file_path, "r"):
            pass
    except FileNotFoundError:
        log_error_then_exit("No such file available! Check file name and extension is typed correctly.")


def get_file_type(file_path: str) -> str:
    """
    Get file type.
    """

    file_path = str(file_path).strip().casefold()
    the_type = "Javascript" if file_path.endswith(".js") else "Unsupported"

    return the_type


def validate_file_type(file_path: str) -> str:
    file_type = get_file_type(file_path)

    if file_type == "Unsupported":
        log_error_then_exit("Our tool only works with Javascript files.")

    return file_type


def log_error_then_exit(error_message: str) -> None:
    """
    Logs the error_message in console then terminates the program execution.
    """

    console.log(f"[red]{error_message}", end="\n\n")
    sys.exit(0)


def print_code_metadata(file_path: str) -> None:
    with open(file_path, "r") as file:
        lines = file.readlines()

        print(f"[+] Total {len(lines)} lines of code.")
        print("[+] Code inside:-")


def get_default_syntax_object(code: str, lang: str, line_to_highlight: Set[int] = None) -> Syntax:
    return Syntax(
        code=code,
        lexer=lang,
        line_numbers=True,
        highlight_lines=line_to_highlight,
        theme="github-dark",
        background_color="default",
    )


def print_code(file_path: str) -> None:
    """
    Takes file path and print code statements line by line.
    """

    print_code_metadata(file_path)

    with open(file_path, "r") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            console.print(f"\t{i+1}. {lines[i]}", end="")

    print("\n")


def print_code_with_rich(file_path: str, line_to_highlight: Set[int]) -> None:
    """
    Prints code with python's "Rich Syntax" object.
    """

    print_code_metadata(file_path)

    with open(file_path, "rt") as code_file:
        code = code_file.read()
        syntax = get_default_syntax_object(code, "javascript", line_to_highlight)
        console.print(syntax)

    print("\n")


def print_error_info(error_info: dict) -> None:
    error_info.pop("traceback")
    error_info.pop("code")

    console.print("[+] Summarized Traceback:- ")
    error_info = json.dumps(error_info, indent=4)
    syntax = get_default_syntax_object(error_info, "json")
    console.print(syntax)

    print("", end="\n")


def print_stackoverflow_answers(answers):
    """
    Hide the logic of printing answers.
    """

    if not answers:
        print("JS-CID could not find answers for the error on StackOverflow!")
    else:
        for i, ans in enumerate(answers):
            print(f"Solution {i+1}:\n")
            console.print(Markdown(ans))
            print("\n")
