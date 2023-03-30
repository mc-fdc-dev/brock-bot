FROM python:3

WORKDIR /app/brock_bot

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install --only main --no-root

COPY . .

CMD ["python", "main.py"]