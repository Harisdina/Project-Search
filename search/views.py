from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import lxml
# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.bing.com/search?q=' + search
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')

        result_listings = soup.find_all('li', class_='b_algo')

        final_result = []

        for result in result_listings:
            result_title = result.find('h2').text
            result_url = result.find('a')['href']
            result_desc = result.find('p').text

            final_result.append((result_title, result_url, result_desc))

        context = {
            'final_result': final_result
        }

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')
