from subprocess import Popen, PIPE
from collections import defaultdict
from dis import get_instructions
from pprint import pprint
import sys
from typing import Union


def get_error_info(file_path: str, stderr=None) -> Union[dict, None]:
    '''
    Summarizes and returns all error information we have in this script/code.
    '''

    if stderr:
        traceback = stderr
    else:
        traceback = get_traceback_from_script(file_path)
        if not traceback:
            return None

        error_message = get_error_message(traceback)
        error_type = get_error_type(error_message)
        error_line = get_error_line_number(traceback)
        file_name = get_file_name(traceback)
        code = get_code(file_path)
        offending_line = get_offending_line(error_line, code)

        error_info = {
            "traceback": traceback,
            "message": error_message,
            "type": error_type,
            "line": error_line,
            "offending_line": offending_line,
            "file": file_name,
            "code": code,
        }

        if not all(error_info.values()):
            print("Missing some data about error!!")
            pprint(error_info)
            sys.exit(-1)

        return error_info


def get_traceback_from_script(file_path: str) -> Union[str, None]:
    """
    Returns the stdout and stderr by executing inside a subprocess.
    """

    command = "node " + str(file_path)
    subprocess = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout = subprocess.stdout.read().decode("utf-8")
    stderr = subprocess.stderr.read().decode("utf-8")
    subprocess.kill()

    if stdout == 'undefined':
        undefined_message = "My be you are trying to access a value that is not defined or assigned yet."
        print(undefined_message)

    # return_1 for testing this method, return_2 is for implementing the actual algorithm
    return_1: dict = {"stdout": stdout, "stderr": stderr}
    return_2: Union[str, None] = stderr or None
    return return_2


def get_error_message(traceback: str) -> str:
    """
    Input: Error message like "TypeError: Assignment to constant variable."
    Output: TypeError
    """

    # traceback = get_traceback_from_script(file_path)["stderr"].splitlines()
    error_lines = traceback.splitlines()

    return error_lines[4][:-1] or None


def get_error_type(error_message: str) -> Union[str, None]:
    '''
    Returns the error as a noun. Implementation Incomplete.
    '''

    error_type = error_message.split(":")[0]

    return error_type


def get_error_line_number(traceback: str) -> int:
    """
    Returns the line number from traceback at where the error line exists.\n
    """

    first_error_line = traceback.splitlines()[0]
    error_line_number = first_error_line.split(':')[2]

    return int(error_line_number)


def get_file_name(traceback) -> str:
    '''
    Get the file name where the error originates.
    '''

    error_lines = traceback.splitlines()
    full_file_path_with_error_line_number = error_lines[0]
    file_full_path_without_directory = full_file_path_with_error_line_number.split(':')[1]
    splitted = file_full_path_without_directory.split('\\')
    file_name = splitted[-1]

    return file_name


def get_file_type(file_path: str) -> str:
    """
    Get file type.
    """
    
    file_path = str(file_path).strip().casefold()
    the_type = "Javascript" if file_path.endswith(".js") else "Unsupported"

    return the_type


def get_code(file_path: str) -> str:
    """
    Gets the source code of the specified file.
    """

    try:
        with open(file_path, "r") as file:
            code = file.read()
    except FileNotFoundError:
        print("No such file available.")
        sys.exit(0)

    return code


def get_offending_line(error_line: int, code: str) -> str:
    '''Extracts the offending line.'''

    error_line -= 1
    code_lines = code.splitlines()
    offending_line = None

    try:
        offending_line = code_lines[error_line]
    except IndexError:
        offending_line = code_lines[-1]

    return offending_line
