from service import get_algorithm_result, save_knowledge_base
from assistant import open_ai_chatbot


def chat_bot(user_input: str) -> str:
    answer = get_algorithm_result(user_input)
    if isinstance(answer, str):
        return answer
    assisted_answer = open_ai_chatbot(user_input)
    answer["questions"].append({"question": user_input, "answer": assisted_answer})
    save_knowledge_base("knowledge_base.json", answer)
    return assisted_answer
