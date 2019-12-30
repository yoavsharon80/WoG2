FROM python:alpine
COPY . /WoG2
WORKDIR /WoG2
RUN pip install -r requirments.txt
CMD [ "python", "MainScores.py" ]
