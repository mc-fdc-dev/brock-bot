FROM python:3

WORKDIR /app/brock_bot

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install --only main --no-root

COPY . .

CMD ["python", "main.py"]
