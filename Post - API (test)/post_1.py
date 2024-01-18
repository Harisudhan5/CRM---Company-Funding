import requests

client_id = '1000.WO2TEXO944G3N8OMAWP9VOKWREPKMY'
client_secret = 'a396850cdd12671c1ad483f833532f4f24b93f3d62'
code = '1000.341219efe5336d44e7637953d1015960.365c2f775c0f601eca9921c7fb0e5503'

token_type = 'Bearer'
expires_in = '3600'

token_url = 'https://accounts.zoho.com/oauth/v2/token'

payload = {
    'code': code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': 'your_redirect_uri',
    'grant_type': 'authorization_code'
}

response = requests.post(token_url, data=payload)

if response.status_code == 200:
    data = response.json()
    access_token = data
    refresh_token = data["refresh_token"]
    print(f'Access Token: {access_token}')
    print(f'Refresh Token:')
    print(f'Token Type: {token_type}')
    print(f'Expires in :{expires_in}')
else:
    print(f'Error: {response.status_code} - {response.text}')
