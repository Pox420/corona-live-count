from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.content, 'html.parser')

all_cases = soup.select('#maincounter-wrap')[0].find('div').find('span').getText()
ac = int(all_cases.replace(',',''))

all_death = soup.select('#maincounter-wrap')[1].find('div').find('span').getText()
ad = int(all_death.replace(',',''))


all_recover = soup.select('#maincounter-wrap')[2].find('div').find('span').getText()
ar = int(all_recover.replace(',',''))


active_cases = ac - ad - ar
actv = f"{active_cases:,}"


def index(request):
    context = {
        'total_cases':all_cases,
        'total_death':all_death,
        'total_recover':all_recover,
        'active_cases':actv,
    }
    return render(request,'index.html',context)