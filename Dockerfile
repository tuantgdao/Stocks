FROM python
ENV PYTHONPATH=$PYTHONPATH:/testService/Stocks
COPY . /testService
WORKDIR /testService
RUN pip install -r requirements.txt
CMD sh