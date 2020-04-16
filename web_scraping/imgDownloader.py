#! python3
# imgDownloader.py - searches for a category of photos (jpg/png) and downloads the resulting images

import os, requests, bs4

def img_download(extension):
    """Search for and download all images of the argument type from Imgur."""
    url = 'http://imgur.com/search?q=' + extension
    os.makedirs('<directory>', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imgElem = soup.select('.post > .image-list-link img')

    for i, img in enumerate(imgElem):
        # Convert image URL from thumbnail size to full-size version
        imgUrl_s = 'https:' + image_elem[i].get('src')
        imgUrl = imgUrl_s[:-5] + '.' + extension

        print('Downloading image {}'.format(imgUrl))
        res = requests.get(imgUrl)
        res.raise_for_status()
        imgFile = open(os.path.join('<directory>', os.path.basename(imgUrl)), 'wb')

        for chunk in res.iter_content(1000000)
            imgFile.write(chunk)
        imgFile.close()

    return len(imgElem)

extension = input('Enter desired file extension')
download = img_download(extension)

if download == 0:
    print('No images found.')
else:
    print('All ' + str(download) + ' files successfully downloaded.')
