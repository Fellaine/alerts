from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def alerts_view(request, *args, **kwargs):

    url = "https://t.me/s/air_alert_ua"
    channel = requests.get(url).text
    soup = BeautifulSoup(channel, 'lxml')
    tgpost = soup.find_all('div', class_='tgme_widget_message')
    full_message = {}
    obj = []

    for content in tgpost:
        full_message['views'] = content.find('span', class_='tgme_widget_message_views').text
        full_message['timestamp'] = content.find('time', class_='time').text
        full_message['text'] = content.find('div', class_='tgme_widget_message_text').text
        tmp = full_message['text']
        #print(tmp[2:tmp.find('#')])
        obj.append(tmp[2:tmp.find('#')])

    context = {"object": obj}
    return render(request, "main.html", context)