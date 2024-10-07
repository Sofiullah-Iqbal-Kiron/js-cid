from argparse import Namespace
from slugify import slugify

from .utils import SEARCH_URL, HINT_MESSAGES


def handle_error(error_info: dict):
    """
    Process the incoming error as needed and returns possible answers.\n\n

    Output:
    query = an URL containing a stackoverflow query about the error
    jscid_hint = a possible answer for the error from this tool locally
    """

    query = None
    jscid_hint = None

    error_type = error_info["type"]
    error_message = error_info["message"]
    error_line = error_info["line"]

    if error_type == "TypeError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["TypeError"].replace('<line_number>', str(error_line))

    elif error_type == "RangeError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["RangeError"].replace('<line_number>', str(error_line))

    elif error_type == "ReferenceError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["ReferenceError"].replace('<line_number>', str(error_line))

    elif error_type == "SyntaxError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["SyntaxError"].replace('<line_number>', str(error_line))

    elif error_type == "InternalError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["InternalError"].replace('<line_number>', str(error_line))

    elif error_type == "URIError":
        print("Handled URIError.")
        jscid_hint = HINT_MESSAGES["URIError"].replace('<line_number>', str(error_line))

    elif error_type == "EvalError":
        query = type_error_query(error_message)
        jscid_hint = HINT_MESSAGES["EvalError"].replace('<line_number>', str(error_line))

    else:
        pass

    return query, jscid_hint


def type_error_query(error_message: str) -> str:
    """
    Process TypeError and returns search query.
    """

    slugged = slugify(error_message, separator="+")
    return get_processed_url(slugged)


def range_error_query(error_message: str) -> str:
    """
    Process RangeError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def reference_error_query(error_message: str) -> str:
    """
    Process ReferenceError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def syntax_error_query(error_message: str) -> str:
    """
    Process SyntaxError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def internal_error_query(error_message: str) -> str:
    """
    Process InternalError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def uri_error_query(error_message: str) -> str:
    """
    Process URIError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def eval_error_query(error_message: str) -> str:
    """
    Process EvalError and returns search query.
    """

    slugged = slugify(error_message, separator='+')
    return get_processed_url(slugged)


def get_processed_url(slugged: str):
    """
    Build a valid search url.
    """

    return SEARCH_URL + get_query_params(slugged)


def get_query_params(slugged: str):
    """
    Prepare the query, include necessary filters.
    """

    order = "&order=desc"
    sort = "&sort=relevance"
    js_tagged = "&tagged=javascript"
    intitle = f"&intitle={slugged}"

    return order + sort + js_tagged + intitle
