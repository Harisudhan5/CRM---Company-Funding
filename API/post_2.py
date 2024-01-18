import requests
api_endpoint = 'https://www.zohoapis.com/crm/v2/Leads'
access_token = '1000.82c9561b7abd27f4fab65a9cde1849c0.5a54cfe3f07c63d4c118b2a14e78f6bc'


lead_data = {
  "data": [
    {
      "Company": "Example Company",
      "Last_Name": "Domyyyyyoe",
      "First_Name": "John",
      "Email": "johndoe@example.com",
      "Phone": "+1234567890"
    }
  ]
}


headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}


response = requests.post(api_endpoint, json=lead_data, headers=headers)


if response.status_code == 201:
    print("Lead inserted successfully.")
    lead_id = response.json()["data"][0]["details"]["id"]
    print(f"Lead ID: {lead_id}")
else:
    print(f"Error: {response.status_code} - {response.text}")
