from bs4 import BeautifulSoup
import requests

class Search():
    def __init__(self, url):
        self.current_url = url
        self.text = ""


    def setup(self,markup, parser):
        self.soup = BeautifulSoup(markup, parser)
        return self.soup

        

# url for the root page
#url = input("Enter the URL: ")
url = "https://lambdaschool.com/"

# get the response from the page
response = requests.get(url)
text = response.text

# instantiate a beautiful soup object
soup = BeautifulSoup(text, 'html.parser')
page = soup.find_all('section')
print(page)



