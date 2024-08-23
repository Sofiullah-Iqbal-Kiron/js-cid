import requests
from typing import Tuple
from operator import attrgetter
from rich import print
from html2text import html2text

from .utils import ANSWERS_URL, Question, Answer


def get_answers(query: str, error_info: dict):
    """
    This coordinate the answer aquisition process.
    - use the query to check stackexchange API for related questions
    - if stackoverflow API search engine couldn't find questions, ask google instead
    - for each question, get the most voted and accepted answers
    - sort answers by vote count and limit them
    - todo: summarize long answers and make it ready to output to the user
    """

    # questions = answers = None
    questions, answers = ask_live(query, error_info)
    sorted_answers = sorted(answers, key=attrgetter("score"), reverse=True)[:5]
    summarized_answers = []

    for ans in sorted_answers:
        markdown_body = html2text(ans.body)
        summarized_answers.append(markdown_body)

    return summarized_answers, sorted_answers


def ask_live(query: str, error_info: dict):
    """
    Retrieve related questions and its answers by making actual http request.
    """

    questions = ask_stackoverflow(query)
    answers = get_answer_content(questions)

    return questions, answers


def ask_stackoverflow(query):
    """
    Ask stackoverflow API for related questions via query.
    """

    if query is None:
        return tuple()
    
    json_response = requests.get(query).json()
    questions = list()

    for question in json_response["items"]:
        if question["is_answered"]:
            questions.append(Question(id=str(question["question_id"]), has_accepted="accepted_answer_id" in question))
    
    return tuple(questions)


def get_answer_content(questions: Tuple[Question]) -> Tuple[Answer, None]:
    """
    Retrieve the most voted and the accepted answers for each question.
    """
    
    answers = []

    for question in questions:
        response = requests.get(ANSWERS_URL.replace("<id>", question.id))
        items = response.json()["items"]
        if items == []:
            continue

        # retrieve most voted
        # first one, cause results are retrieved in sorted by score
        most_voted = items[0]

        current_answer = Answer(
            id=str(most_voted["answer_id"]),
            accepted=most_voted["is_accepted"],
            score=most_voted["score"],
            body=most_voted["body"],
            author=most_voted["owner"]["display_name"],
        )
        answers.append(current_answer)

        if most_voted["is_accepted"]:
            continue

        filtered = list(filter(lambda a: a["is_accepted"], items))
        if filtered == []:
            continue

        accepted = filtered[0]
        answers.append(
            Answer(
                id=str(accepted["answer_id"]),
                accepted=True,
                score=accepted["score"],
                body=accepted["body"],
                author=accepted["owner"]["display_name"],
            )
        )

    return answers
