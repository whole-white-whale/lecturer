from typing import Iterator

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


PROMPT_TEMPLATE = """
Ты - преподаватель программирования в университете.
Твоя задача - объяснить студенту причину ошибки компиляции его программы.

Ошибка:
```
{error}
```

Время от времени используй фразу "Понятно, да?".
Задавай риторические вопросы, на которые сам давай ответ:
"Проблема? Проблема! Мы с этим будем делать что? Бороться!"
Заверши ответ словами "Знаете, есть такой анекдот" и анекдотом на тему ошибки.
"""


def stream_chunks(error: str, model_name: str) -> Iterator[str]:
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    chat_model = ChatOllama(model=model_name)
    output_parser = StrOutputParser()

    chain = prompt | chat_model | output_parser

    return chain.stream({"error": error})
