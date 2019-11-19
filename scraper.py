import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.jumia.co.ke/sony-computer-entertainment-new-fifa-20-ps4-24665176.html'

headers = {
    "User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 '
                  'Safari/537.36'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ikariuki741@gmail.com', 'xbaioisvdfuxfrhq')

    subject = 'Hey Ian The Price fell down'

    body = 'Check the Jumia link' \
           ' https://www.jumia.co.ke/sony-computer-entertainment-new-fifa-20-ps4-24665176.html'

    msg = f"Subject:{subject} \n\n Body:{body}"

    server.sendmail(
        'ikariuki741@gmail.com',
        'ikariuki741@gmail.com',
        msg
    )

    print("HEY EMAIL HAS BEEN SENT")

    server.quit()


def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="-fs20 -pts -pbxs").get_text()
    price = soup.find(class_="-b -ltr -tal -fs24").get_text().replace(",", "")
    converted_price = int(price[4:9])
    print('Checking Prices...')
    if converted_price <=5100:
        send_mail()
        print(title)
        print(converted_price)


while True:
    checkPrice()
    time.sleep(60 * 60)
