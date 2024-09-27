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
from jscid.gemini import geminiSolution
from jscid.stackoverflow import stackoverflowSolution


# rich console app
console = Console()


def main(file_name: str) -> None:
    """
    Takes fully specified relative path of the file to detect bugs and return possible solutions using Gemini and StackOverflow API.
    """

    # check that specified file is exists in the operating system or not
    check_availability(file_name)

    file_type = validate_file_type(file_name)
    print("", end="\n")
    console.rule("[bold red]JS-CID")
    print(f'[+] "{file_type}" file detected.', end="\n\n")

    error_at_line = None
    error_info = get_error_info(file_name)
    if error_info:
        error_at_line = error_info["line"]
    
    # print actual code inside the file
    print_code_with_rich(file_name, set([error_at_line]))

    # print summarized error message if occurs
    if error_info:
        print_error_info(error_info)
    else:
        console.log("[green]Yep! seems your script has no error :computer:\n")
        sys.exit(0)

    # progress bar indicating generating solutions
    # if solution fetching success then rule.
    console.rule("[bold red]Possible Solutions")
    stackoverflowSolution(file_name)
    geminiSolution(file_name)


if __name__ == "__main__":
    typer.run(main)
