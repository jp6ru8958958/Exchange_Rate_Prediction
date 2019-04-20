import requests
from bs4 import BeautifulSoup

class Crawler():

    def __init__(self, url):
        self.URL = url
        self.Response = requests.get(url)

    def print_current_state(self):
        self.Response.encoding = 'Utf-8'
        print("link:",self.URL)
        print("state:",self.Response.status_code)
        print(self.Response.text)

    def call_bs4(self):
        self.soup = BeautifulSoup(self.Response.text, "html.parser")
