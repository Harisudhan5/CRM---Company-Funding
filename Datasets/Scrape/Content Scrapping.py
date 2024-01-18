from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv
no_of_company = int(input("Enter no of company : "))
url_file = input("Enter url file name :")
final_destination = "new.csv"
cnt = 1
with open(url_file,"r") as file:
    reader = csv.reader(file)
    data = list(reader)
    c = 1
    for ptrs in range(0,no_of_company):
        c_url = data[ptrs][0]
        ul = c_url
        reqs = Request(
            url=ul,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        webpage = urlopen(reqs)
        soup = BeautifulSoup(webpage,"html.parser")
        tite = soup.find("h1",class_="entry-title").text
        inner_box = soup.find_all("div",class_="detail")
        description = soup.find("div",class_="et_pb_text_inner").h2.text
        # <div class="et_pb_module et_pb_text et_pb_text_1  et_pb_text_align_left et_pb_bg_layout_light company-dynamic-text">
        p1,p2,p3,p4,p5,p6,p7 = 0,0,0,0,0,0,0
        
        for i in range(len(inner_box)):
            if str(inner_box[i].label.text).strip() == "Number of Employees:":
                employee_count = inner_box[i].a.text
                p1 = 1
            elif str(inner_box[i].label.text).strip() == "Leaders:":
                try:
                    leader = inner_box[i].a.text
                    p0 = 1
                except:
                    leader = "Null"
                try:
                    lead_dtail = inner_box[i].a["href"]
                except:
                    lead_dtail = "Null"
            elif str(inner_box[i].label.text).strip() == "Funding:":
                funding_type = inner_box[i].a.text
                p2 = 1
            #elif str(inner_box[i].label.text).strip() == "Office Locaation:":
            #    location = inner_box[i].a.text
            elif str(inner_box[i].label.text    ).strip() == "Founded:":
                founded = inner_box[i].text
                founds = founded.split(":")
                founded = founds[-1].strip()
                p3 = 1
            elif str(inner_box[i].label.text).strip() == "Software Type:":
                software_type = inner_box[i].a.text
                p4 = 1
            elif str(inner_box[i].label.text).strip() == "Industry:":
                industry_type = inner_box[i].a.text
                p5 = 1
                    #<label>Industry:&nbsp;</label>      <a href="https://gregslist.com/austin/software-companies-industry/education/" data-toggle="tooltip" data-placement="top" title="" data-wpel-link="internal" data-original-title="More Education Companies">Education</a>
            elif str(inner_box[i].label.text).strip() == "Category:":
                cate = inner_box[i].a.text
                p6 = 1
            elif str(inner_box[i].label.text).strip() == "Size:":
                size = inner_box[i].a.text
                p7 = 1
            elif str(inner_box[i].label.text).strip() == "Website:":
                website = inner_box[i].a.text
            elif str(inner_box[i].label.text).strip() == "Linkedin:":
                linkedin = inner_box[i].a.text
            elif str(inner_box[i].label.text).strip() == "Address:":
                address = inner_box[i].a.text
                lis_cntry = ["Atlanta","Austin","Boston","Chicago","Dallas","Denver","Houston","Phoenix","Raleigh-Durham","Salt Lake City","San Diego","Tornoto"]
                for i in lis_cntry:
                    if i in address:
                        city = i
        print("\--------(",cnt,")----------->\n")
        cnt = cnt + 1
        if p1 != 0 and p2 != 0 and p3 != 0  and p4 != 0 and p5 != 0 and p6 != 0 and p7 != 0:
            nt = "Null"
            print("0",tite)
            try:
                print("1",leader)
            except:
                leader = nt
                print("1",leader)
            try:
                print("2",employee_count)
            except:
                employee_count = nt
                print("2",employee_count)
            try:
                print("3",funding_type)
            except:
                funding_type = nt
                print("3",funding_type)
            try:
                print("5",founded)
            except:
                founded = nt
                print("5",founded)
            try:
                print("6",software_type)
            except:
                software_type = nt
                print("6",software_type)
            
            try:
                print("8",cate)
            except:
                cate = nt
                print("8",cate)
            try:
                print("7",industry_type)
            except:
                industry_type = nt
                print("7",industry_type)
            try:
                print("9",size)
            except:
                size = nt
                print("9",size)
            try:
                print("10",website)
            except:
                website = nt
                print("10",website)
            try:
                print("11",linkedin)
            except:
                linkedin = nt
                print("11",linkedin)
            try:
                print("12",address)
            except:
                address = nt
                print("12",address)
            try:
                print("13",description)
            except:
                description = nt
                print("13",description)
            try:
                print("14",city)
            except:
                city = nt
                print("14",city)
            try:
                print("15",lead_dtail)
            except:
                lead_dtail = nt
                print("15",lead_dtail)
            groupd = [
                [tite,leader,lead_dtail,employee_count,funding_type,founded,software_type,industry_type,cate,size,website,linkedin,city,address,description]
            ]

            with open(final_destination,"a",encoding = "utf-8",newline = "") as f3:
                writ = csv.writer(f3)
                writ.writerows(groupd)
        else:
            print("=======(Contains Null Value)==============>")

