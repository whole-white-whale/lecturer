# lecturer

## Установка

Для работы с большими языковыми моделями понадобится Ollama.
Скачать её можно с [официального сайта](https://ollama.com/download).

По умолчанию приложение использует модель `llama3.1`.
Скачать её можно следующим образом:

```bash
ollama pull llama3.1
```

Собрать приложение удобнее всего с помощью Poetry:

```bash
poetry install && poetry build
pip install dist/lecturer-0.1.0-py3-none-any.whl
```

## Использование

Достаточно перенаправить вывод сообщений об ошибках компиляции:

```bash
gcc ... |& python -m lecturer
```
