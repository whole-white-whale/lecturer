import sys

import fire

from lecturer import stream_chunks


def cli():
    fire.Fire(run)


def run(*, model_name: str = "llama3.1"):
    for chunk in stream_chunks(error=sys.stdin.read(), model_name=model_name):
        print(chunk, end="", flush=True)
