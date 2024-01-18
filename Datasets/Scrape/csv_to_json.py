import csv
import json

csv_file = 'greglist_data_crm.csv'

json_file = 'output.json'

data = []
list_of_country = []

with open(csv_file, 'r') as csvf:
    csv_reader = csv.DictReader(csvf)
    ct = 0
    for row in csv_reader:
        row["Lead Source"] = "Gregslist"
        if ct == 65:
            break
        else:
            ct = ct + 1
            for ctr in list_of_country:
                if ctr in country:
                    country = row["Address"]
            
            data.append(row)


with open(json_file, 'w') as jsonf:
    json.dump(data, jsonf, indent=4)

print(f'CSV file "{csv_file}" has been converted to JSON file "{json_file}"')
