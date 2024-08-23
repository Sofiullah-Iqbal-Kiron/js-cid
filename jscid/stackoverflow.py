from .inspection import get_error_info
from .errors import handle_error
from .answers import get_answers
from .utils import print_stackoverflow_answers


def stackoverflowSolution(file_path: str) -> None:
    error_info = get_error_info(file_path)
    query, jscid_hint = handle_error(error_info)
    answers, _ = get_answers(query, error_info)
    print_stackoverflow_answers(answers)
