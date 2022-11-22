FROM python:3.10-slim


ADD ./ /src-backend

WORKDIR /src-backend

# RUN python3 -m venv src-env && \
#     . ./src-env/bin/activate && \
#     # apt-get update -y && apt-get install make build-essential libssl-dev zlib1g-dev \
#     # libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
#     # libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y && \
#     # apt-get update -y && \
#     # apt-get install default-libmysqlclient-dev -y && \
#     pip install pipenv gunicorn gevent && \
#     pipenv install --dev && \
#     chmod +x ./start.sh




CMD ["./start.sh"]