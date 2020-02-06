FROM python
COPY . /testService
WORKDIR /testService
ENV PYTHONPATH /testService
ENV FLASK_APP index.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
CMD ["flask", "run"]