from .inspection import get_error_info
from .errors import handle_error
from .answers import get_answers
from .utils import get_code, print_stackoverflow_answers
from .ranking import rank_by_levenshtein


def stackoverflowSolution(file_path: str) -> None:
    error_info = get_error_info(file_path)
    query, jscid_hint = handle_error(error_info)
    print(query)
    answers, _ = get_answers(query, error_info)
    ranked_answers = rank_by_levenshtein(answers, get_code(file_path))
    print_stackoverflow_answers(ranked_answers)
