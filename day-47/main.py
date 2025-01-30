from email import header
from bs4 import BeautifulSoup
import requests
import smtplib

sender_email = "ashenafipaul21@gmail.com"
receiver_email = "apawlos0@gmail.com"
app_password = ""

url = "https://www.amazon.com/Wicked-Ultra-Blu-ray-Digital-UHD/dp/B0DNLMFDX7/?_encoding=UTF8&pd_rd_w=alI9q&content-id=amzn1.sym.41f1b87d-2e7a-4fe4-bfcc-e038cab8f79e&pf_rd_p=41f1b87d-2e7a-4fe4-bfcc-e038cab8f79e&pf_rd_r=TADM8PD1YWW6DY03MPC3&pd_rd_wg=PixGz&pd_rd_r=c774bd8a-e0a7-43ae-bf4e-5e57864c530c&ref_=pd_hp_d_btf_crs_zg_bs_2625373011"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(name="span", class_="a-price-whole")
price = price.getText()

actual_price = int(price.split(".")[0])

try:
    if actual_price < 30:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=app_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=f"Subject:Price Alert\n\nThe price for Wicked Ultra HD Blu-ray is now ${actual_price}."
            )
        print("Email sent.")
    else:
        print("Price is still high.")
except Exception as e:
    print(e)
    print("Error sending email.")