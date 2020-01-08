FROM python:3.6-slim
RUN mkdir /intercom
WORKDIR /intercom
COPY . /intercom
CMD python3 customers_in_range.py; python3 -m unittest discover
