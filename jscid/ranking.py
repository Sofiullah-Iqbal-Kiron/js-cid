from typing import List
from strsimpy.levenshtein import Levenshtein
from .utils import Answer


class R_Answer:
    def __init__(self, distance, answer: Answer) -> None:
        self.distance = distance
        self.answer = answer


levenshtein = Levenshtein()


def rank_by_levenshtein(to_rank: List[Answer], to_compare: str):
    r_answers = list()

    for item in to_rank:
        distance = levenshtein.distance(item, to_compare)
        new_r_answer = R_Answer(distance, item)
        r_answers.append(new_r_answer)

    r_answers = sorted(r_answers, key=lambda x: x.distance)

    return r_answers
