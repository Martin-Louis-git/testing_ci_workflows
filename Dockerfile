# syntax=docker/dockerfile:1

FROM python:3.11.9

COPY . .

RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv","run", "app/main.py"]
