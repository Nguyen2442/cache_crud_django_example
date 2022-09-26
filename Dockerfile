FROM python:3.10-slim


ADD ./ /src-backend

WORKDIR /src-backend

RUN python3 -m venv src-env && \
    . ./src-env/bin/activate && \
    pip install pipenv gunicorn gevent && \
    pipenv install --dev && \
    chmod +x ./start.sh


CMD ["./start.sh"]