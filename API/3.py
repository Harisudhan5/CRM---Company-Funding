import requests
def post2():
    try:
        id = "1000.WO2TEXO944G3N8OMAWP9VOKWREPKMY"
        secret = "a396850cdd12671c1ad483f833532f4f24b93f3d62"
        cd = "1000.5c08f8c211e36a880e62f74fcb1acac0.ef410ef5822f118aed8babafae32a0bb"
        dat =  {     "data": [         {             "Company": "Example Company",             "Last_Name": "Doe",             "First_Name": "John",             "Email": "johndoe@example.com",             "Phone": "+1234567890"         }     ] }
        # Define the OAuth2 credentials and the authorization code
        client_id = id
        client_secret = secret
        code = cd


        token_type = 'Bearer'
        expires_in = '3600'

        # Define the token URL
        token_url = 'https://accounts.zoho.com/oauth/v2/token'

        # Define the payload for the POST request
        payload = {
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': 'your_redirect_uri',
            'grant_type': 'authorization_code'
        }

        # Send the POST request to obtain tokens
        response = requests.post(token_url, data=payload)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            access_token = data['access_token']
            refresh_token = data['refresh_token']
            print(f'Access Token: {access_token}')
            print(f'Refresh Token: {refresh_token}')
            print(f'Token Type: {token_type}')
            print(f'Expires in :{expires_in}')
            api_endpoint = 'https://www.zohoapis.com/crm/v2/Leads'
            access_token = '1000.82c9561b7abd27f4fab65a9cde1849c0.5a54cfe3f07c63d4c118b2a14e78f6bc'


            lead_data = dat


            headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
            }


            res = requests.post(api_endpoint, json=lead_data, headers=headers)


            if res.status_code == 201:
                print("Lead inserted successfully.")
                lead_id = res.json()["data"][0]["details"]["id"]
                print(f"Lead ID: {lead_id}")
                return "yessss successfully added"
            else:
                return "not inserted"
        else:
            return "credentials error"

    except:
        return "Errors not in loops"
post2()