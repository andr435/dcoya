FROM python:3
WORKDIR /usr/src/app/dcoya

COPY ./dcoya .
COPY ./pgdata  ../pgdata

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

