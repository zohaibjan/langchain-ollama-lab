# LangChain and Ollama Learning Lab

Coursework and small experiments for learning LLM application development.

The default `1-start-here` branch contains a biography summarisation exercise: a prompt asks a local Ollama model for a short summary and two facts.

## Components

- `ice_breaker.py`: prompt, model call and string output parser.
- `Pipfile` / `Pipfile.lock`: the original Python 3.11 environment definition.
- `LICENSE`: existing repository licence.

## Running the exercise

1. Set up Python 3.11 and a compatible environment for the imports in `ice_breaker.py`.
2. Install and run Ollama locally, and acquire the `mistral` model used by the script.
3. Review the `information` string and model configuration.
4. Run:

```bash
python ice_breaker.py
```

The script imports `langchain_ollama` and `dotenv`, which are not explicitly listed in the current Pipfile. Resolve those dependencies before running. LangChain APIs have changed since this exercise was written, so environment compatibility needs checking.

## Scope

A learning exercise, with no claim of production deployment, retrieval, agent orchestration or evaluated answer quality. Preserve course and upstream attribution when extending the material.

[Profile and project directory](https://github.com/zohaibjan)
