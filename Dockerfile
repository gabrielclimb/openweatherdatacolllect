FROM public.ecr.aws/docker/library/python:3.11 as python
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install build-essential -y  \
    && apt-get install make -y \
    && apt-get clean

COPY src ./src
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
RUN make pip-install

CMD ["make"]


FROM python
RUN
