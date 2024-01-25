import json
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_matching_question(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base.get("questions", []):
        if q.get("question") == question:
            return q.get("answer")
    return None


def get_algorithm_result(user_input) -> str | dict:
    knowledge_base: dict = load_knowledge_base('algo/knowledge_base.json', )
    best_match: str | None = find_best_matching_question(user_input,
                                                         [q["question"] for q in knowledge_base.get("questions", [])])
    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        return answer
    return knowledge_base
