FROM python:3.13.3

WORKDIR /code

ENV PYTHONPATH=/code/src

ADD ./requirements.txt requirements
RUN pip install -r requirements

COPY ./ /code/

ENTRYPOINT ["tail", "-f", "/dev/null"]