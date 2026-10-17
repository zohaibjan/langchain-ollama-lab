# LangChain and Ollama Learning Lab

Coursework and small experiments for learning LLM application development.

The default `1-start-here` branch contains a biography summarisation exercise: a prompt asks a local Ollama model for a short summary and two facts.

## Components

- `ice_breaker.py`: prompt, model call and string output parser.
- `Pipfile` / `Pipfile.lock`: the original Python 3.11 environment definition.
- `LICENSE`: existing repository licence.

## Running the exercise

Use Python 3.11+ and a fresh virtual environment:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
# Install/run Ollama separately, then pull the configured model:
ollama pull mistral
python ice_breaker.py
```

The direct dependencies above match the current `langchain_core` and `langchain_ollama` imports. `Pipfile` and `Pipfile.lock` remain historical coursework artifacts and do not define this refreshed environment. The bundled biography is historical sample text, not a current factual profile.

Offline prompt/chain checks use a fake runnable and require no Ollama server:

```bash
python -m unittest discover -s tests -v
```

Those checks validate prompt substitution, missing-input handling and output parsing. A real Ollama generation was not exercised during this cleanup.

## Scope

A learning exercise, with no claim of production deployment, retrieval, agent orchestration or evaluated answer quality. Preserve course and upstream attribution when extending the material.

[Profile and project directory](https://github.com/zohaibjan)
