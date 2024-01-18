import requests

# Define your Zoho CRM API credentials
client_id = '1000.WO2TEXO944G3N8OMAWP9VOKWREPKMY'
client_secret = 'a396850cdd12671c1ad483f833532f4f24b93f3d62'
access_token = '1000.ddba8c96d8852caf9e905652b1ec7995.17c0b1d2a8b4625a9d130bca52ec3e9c'  # You can obtain this token using OAuth 2.0 flow
zoho_crm_api_url = 'https://www.zohoapis.com/crm/v2/Leads'

# Define the lead data
lead_data = {
    "data": [
        {
            "Last_Name": "Doe",
            "First_Name": "John",
            # Add other lead data here
        }
    ]
}

# Set the headers for the API request
headers = {
    'Authorization': f'Zoho-oauthtoken {access_token}',
    'Content-Type': 'application/json'
}

# Make the API request to create the lead
response = requests.post(zoho_crm_api_url, json=lead_data, headers=headers)

# Check the response
if response.status_code == 201:
    print("Lead added successfully!")
else:
    print("Failed to add lead. Status code:", response.status_code)
    print("Response content:", response.content)
