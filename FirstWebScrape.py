import requests
from bs4 import BeautifulSoup

#URL of the events page
url = 'https://www.python.org/events/'
req = requests.get(url)

#Parse the HTML content
soup = BeautifulSoup(req.text, 'lxml')


#Find the event list
events = soup.find('ul', {'class':'list-recent-events'}).find_all('li')

#Loop through the events and print details
for event in events:
    title = event.find('h3').get_text(strip=True)
    location = event.find('span',
                          {'class': 'event-location'}).get_text(strip=True)
    date = event.find('time').get_text(strip=True)

    print(f'title: {title}')
    print(f'location: {location}')
    print(f'date: {date}')
    print('-' * 40)