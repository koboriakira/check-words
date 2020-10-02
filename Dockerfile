FROM python:3.8.5-slim

WORKDIR work

ADD my_dictionary /work/my_dictionary
# ADD tests /work/tests
# ADD requirements.txt /work/requirements.txt
ADD Pipfile /work/Pipfile
RUN pip install --upgrade pip && \
  pip install --no-cache-dir pipenv && \
  pipenv lock -r > /work/requirements.txt && \
  pip install --no-cache-dir -r requirements.txt

# ADD nltk_data
ADD nltk_setup.py /work/nltk_setup.py
RUN python nltk_setup.py

CMD ["uvicorn","my_dictionary.main:app","--host","0.0.0.0","--port","8080"]
