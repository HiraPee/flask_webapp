FROM python:3.9
WORKDIR /app
#COPY ./app /app
RUN pip install Flask
RUN pip install PyPDF2
RUN pip install requests
RUN pip install requests requests_oauthlib --user
RUN pip install python-dotenv
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install glob2
RUN pip install mecab-python3
RUN pip install wordcloud
RUN pip install matplotlib
# ライブラリのインストール
RUN pip install unidic-lite
# RUN pip install google-cloud-datastore
# CMD ["python", "index.py"]
CMD [ "bash" ]
