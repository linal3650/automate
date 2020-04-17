#! python3
# torrent_launcher - Checks for emailed Magnet links and begins downloading them

import time, subprocess, imapclient, pyzmail

def magnet_check():
    # Checks Gmail for Magnet links from verified address and returns them
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login(BOT_EMAIL, BOT_PASS)
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search(['FROM', VERIFIED_EMAIL])

    magnets = []
    if UIDs:
        for identifier in UIDs:
            rawMessage = imapObj.fetch([identifier], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(rawMessage[identifier][b'BODY[]'])
            subject = message.get_subject()
            #message.text_part.get_payload().decode(message.text_part.charset)

            if VERIFICATION_PASS in subject:
                text = message.text_part.get_payload().decode(message.text_part.charset)
                magnets.append(text)

            #imapObj.delete_messages(UIDs)
            #imapObj.expunge()

        imapObj.logout()

        return magnets

TORRENT_CLIENT = (r'C:\Program Files (x86)\uTorrent\uTorrent.exe')
BOT_EMAIL = input('Please enter your email:\n')
BOT_PASS = input('Please enter your password:\n')
VERIFIED_EMAIL = 'al738@scarletmail.rutgers.edu'
VERIFICATION_PASS = 'Verified Email Address'

while True:
    magnet_links = magnet_check()
    for link in magnet_links:
        subprocess.Popen(TORRENT_CLIENT + ' ' + link)

    time.sleep(60 * 15)
