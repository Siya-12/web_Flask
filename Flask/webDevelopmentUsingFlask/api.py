import os
import nlpcloud
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NLPCLOUD_API_KEY")

class API:
    def perform_ner(self, text, entity):
        client = nlpcloud.Client("lt_core_news_lg", API_KEY, gpu=True)
        return client.entities(text, searched_entity=entity)

    def perform_sentiment(self, text):
        client = nlpcloud.Client("gpt-oss-120b", API_KEY, gpu=True)
        return client.sentiment(text, target="NLP Cloud")

    def perform_emotion(self, text):
        client = nlpcloud.Client("gpt-oss-120b", API_KEY, gpu=True)
        return client.summarization(text, size="small")