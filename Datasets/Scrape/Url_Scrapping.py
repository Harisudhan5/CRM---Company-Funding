from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv


#       https://gregslist.com/austin/search/?filtered=true&paged=

# current pages 11
for x in range(1,6):
    #  Error due to security ---> This is probably because of mod_security or some similar server security feature which blocks known spider/bot user agents (urllib uses something like python urllib/3.3.0, it's easily detected). 
    req1 = Request(
        url='https://gregslist.com/toronto/search/?filtered=true&paged='+str(x), 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    webpage = urlopen(req1)

    soup1 = BeautifulSoup(webpage,"html.parser")
    company = soup1.find_all("div",{"class":"col-md-3 company-logo-column"})

    # et_builder_outer_content > div > div > div > div > div > div.et_pb_column.et_pb_column_3_5.et_pb_column_2.et_pb_css_mix_blend_mode_passthrough
    file = open("tornato_urls.csv","a",newline="")
    writer = csv.writer(file)
    for i in company:
        jk = str(i.a["href"])
        writer.writerow([jk])
















'''from bs4 import BeautifulSoup
import requests

html_user = requests.get("https://gregslist.com/austin/").text
soup = BeautifulSoup(html_user,"html.parser")

body = soup.find("body").div
#inner_body = body.find("div",class_="site")
#comapny_name = inner_box.find("div",{"class":"col-md-3 company-logo-column"})
print(body)'''




'''
req2 = Request(
    ulr="https://gregslist.com/austin/company/2fa-identity-automation", 
    headers2={'User-Agents': 'Mozilla/5.0'}
)
mini_web = urlopen(req2)
soup2 = BeautifulSoup(mini_web,"html.parser")
heads = soup2.body.div
left_side = heads.find("div",class_="et_pb_column_3_5.et_pb_column_2.et_pb_css_mix_blend_mode_passthrough")
type_of_cmpy = left_side.find("h2").text
print(comapany_name)
print(type_of_cmpy)'''