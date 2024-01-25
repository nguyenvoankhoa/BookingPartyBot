from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# api_key = os.getenv("API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

client = OpenAI(api_key="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")


def send_user_message(message_body):
    thread = client.beta.threads.create()
    thread_id = thread.id
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message_body,
    )
    return thread_id


def run_assistant(assist_id: str, thread_id: str) -> str:
    assistant = client.beta.assistants.retrieve(assist_id)
    thread = client.beta.threads.retrieve(thread_id)
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    new_message = messages.data[0].content[0].text.value
    return new_message


def open_ai_chatbot(prompt) -> str | None:
    message = send_user_message(prompt)
    response = run_assistant(assistant_id, message)
    return response
