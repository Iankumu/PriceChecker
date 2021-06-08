import requests
from bs4 import BeautifulSoup
import smtplib
import time
from dotenv import load_dotenv
from decouple import config



URL = 'https://www.jumia.co.ke/sony-ps4-fifa-20-disc-28842211.html'

headers = {
    "User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 '
                  'Safari/537.36'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(config('Email'), config('Password'))

    subject = 'Hey Ian The Price fell down'

    body = 'Check the Jumia link' \
           ' https://www.jumia.co.ke/sony-ps4-fifa-20-disc-28842211.html'

    msg = f"Subject:{subject} \n\n Body:{body}"

    server.sendmail(
        config('Email'),
        config('Email'),
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
    if converted_price <=8000:
        send_mail()
        print(title)
        print(converted_price)


while True:
    checkPrice()
    time.sleep(60 * 60)
