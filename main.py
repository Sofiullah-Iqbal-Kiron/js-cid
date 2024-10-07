# python
import sys

# 3'rd party
import typer  # command line application
from rich import print  # drop-in replacement of built-in print
from rich.console import Console

# local
from jscid.inspection import get_error_info
from jscid.utils import (
    check_availability,
    validate_file_type,
    print_code_with_rich,
    print_error_info,
)
from jscid.stackoverflow import stackoverflowSolution
from jscid.gemini import geminiSolution


console = Console()


def main(file_name: str, msc: int = 5) -> None:
    """
    Takes fully specified relative path of the file to detect bugs and returns possible solutions using Gemini and StackOverflow API.
    """

    check_availability(file_name)

    file_type = validate_file_type(file_name)
    print("", end="\n")
    console.rule("[bold red]JS-CID")
    print(f'[+] "{file_type}" file detected.', end="\n\n")

    error_at_line = None
    error_info = get_error_info(file_name)
    if error_info:
        error_at_line = error_info["line"]
    
    print_code_with_rich(file_name, set([error_at_line]))

    if error_info:
        print_error_info(error_info)
    else:
        console.log("[green]Yep! seems your script has no error :computer:\n")
        sys.exit(0)

    console.rule("[bold red]Stackoverflow")
    stackoverflowSolution(file_name)

    console.rule("[bold red]Gemini")
    geminiSolution(file_name)


if __name__ == "__main__":
    typer.run(main)
