import requests
from bs4 import BeautifulSoup

import os
import smtplib
from email.message import EmailMessage

email_id = os.environ.get("email_addr")
email_pass = os.environ.get("email_pass")


url = "https://www.amazon.in/Apple-iPhone-13-Pro-128GB/dp/B09G91LWTZ/?_encoding=UTF8&pd_rd_w=G88lH&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=26RQSQY14GEG34FZC3QH&pd_rd_wg=rhLBV&pd_rd_r=18d4f4ff-a55c-4725-aabb-aabc1454de5a&ref_=pd_gw_ci_mcx_mr_hp_atf_m"


def chk_price():

    headers = {
    "user-Agents": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="a-size-large product-title-word-break").get_text()
    price = soup.find(class_="a-price-whole").get_text()
    cprice = int((price[0:len(price)-1].replace(",", "")))

    print(title.strip())
    print(cprice)

    if (cprice <= cprice-cprice*0.01 ):
        send_mail()

def send_mail():
    msg= EmailMessage()
    msg['Subject']="product price fell down"
    msg['From']=email_id
    msg['To']=email_id
    msg.set_content("hey check this link:https://www.amazon.in/Apple-iPhone-13-Pro-128GB/dp/B09G91LWTZ/?_encoding=UTF8&pd_rd_w=G88lH&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=26RQSQY14GEG34FZC3QH&pd_rd_wg=rhLBV&pd_rd_r=18d4f4ff-a55c-4725-aabb-aabc1454de5a&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

    with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,email_pass)
        smtp.send_message(msg)
chk_price()
