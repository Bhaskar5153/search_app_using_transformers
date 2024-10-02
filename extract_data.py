import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Augmented_reality#:~:text=Augmented%20reality%20(AR)%20is%20an%20interactive%20experience%20that"

# print(url)

response = requests.get(url=url)
soup = BeautifulSoup(response.content, 'html.parser')

paragraphs = soup.find_all('p')

data = '\n'.join([p.get_text() for p in paragraphs])

# print(len(data))

with open('ar_wiki.txt', mode='w', encoding='utf-8') as f:
    f.write(data)

print("data has been extracted and saved as text file")


    

# print(data)
    





