import csv
import mysql.connector

conn = mysql.connector.connect(host = "",user = 'root',password = "2580",database = "niograph",port = 3306)
cursor = conn.cursor()

print("Succesfully connected")


table_name = 'crms'


csv_file = 'greglist_data_crm.csv'
c = 0
try:
    with open(csv_file, 'r', encoding='utf-8',newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        print("-----")
        
        for row in csv_reader:
            c = c + 1
            s = row
            cname = str(s[0])
            leaders = str(s[1])
            no = str(s[2])
            funding = str(s[3])
            year = str(s[4])
            software = str(s[5])
            industry = str(s[6])
            category = str(s[7])
            sizes = str(s[8])
            website = str(s[9])
            linkedin = str(s[10])
            address = str(s[11])

            insert_query = "INSERT INTO crms (company_name, leaders, no_of_employees, funding_type, year, software, industry, category, size, website, linkedin, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            data = (cname, leaders, no, funding, year, software, industry, category, sizes, website, linkedin, address)
            cursor.execute(insert_query, data)


    print("tsrt")
    conn.commit()
    print("end")

except Exception as e:
    print(f"Error: {str(e)}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()
