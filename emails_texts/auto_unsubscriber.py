#! python3
# auto_unsubscriber.py - Scans emails for unsubscibe links and opens them in a browser

import webbrowser, imaplib, imapclient, bs4, pyzmail

def unsub_scan(user_name, user_pass):
    # Returns a list of the unsubscribe links in a Gmail inbox
    unsub_links = []
    imaplib._MAXLINE = 10000000
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(user_name, user_pass)
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search(['SINCE', '01-Feb-2020'])

    for identifier in UIDs:
        raw_message = imapObj.fetch([identifier], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
        html = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html, 'lxml')
        link_elems = soup.select('a')
        for selected in link_elems:
            if 'unsubscribe' in str(selected):
                unsub_links.append(selected.get('href'))
    imapObj.logout()
    return unsub_links

email = input('Enter your email username: ')
password = input('Enter your email password: ')
links = unsub_scan(email, password)

for link in links:
    webbrowser.open(link)

print('All unsubscribe links have been opened')
