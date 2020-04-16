#! python3
# linkVerification.py - Downloads all linked pages from a given URL and notes any 404 Client Error

import requests, bs4

url = input('Enter the URL that you would like to verify the links for:\n')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
error = []

for link in links:
    try:
        test_url = link['href']
        if test_url.startwith('//'):
            to_check = test_url

        elif test_url.startwith('//'):
            to_check = 'https' + test_url

        elif test_url.startwith('#'):
            to_check = url + test_url

        result = requests.get(to_check)

        if result.status_code == 404:
            error.append(to_check)

    except:
        pass

print('The processed links from your URL input returned ' + str(len(error)) + ' 404 Client URL error')
print('\n'.join(error))
