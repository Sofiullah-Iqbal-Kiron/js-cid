from argparse import Namespace
from slugify import slugify

from .utils import SEARCH_URL


def handle_error(error_info: dict):
    """
    Process the incoming error as needed and outputs three possible answer.\n\n

    Output:
    query = an URL containing a stackoverflow query about the error
    jscid_hint = a possible answer for the error from this tool locally
    """

    # objects to return from this method
    query = None
    jscid_hint = None

    error_type = error_info["type"]
    error_message = error_info["message"]
    error_line = error_info["line"]

    if error_type == "TypeError":
        query = handle_type_error(error_message)
    elif error_type == "RangeError":
        query = handle_type_error(error_message)
    elif error_type == "ReferenceError":
        query = handle_type_error(error_message)
    elif error_type == "SyntaxError":
        query = handle_type_error(error_message)
    elif error_type == "InternalError":
        query = handle_type_error(error_message)
    elif error_type == "URIError":
        print("Handled URIError.")
    elif error_type == "EvalError":
        query = handle_type_error(error_message)
    else:
        pass

    return query, jscid_hint


def handle_type_error(error_message: str) -> str:
    """
    Process TypeError and returns search query.
    """

    slugged = slugify(error_message, separator="+")
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
