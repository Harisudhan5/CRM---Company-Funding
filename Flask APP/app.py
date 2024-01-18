from flask import Flask, render_template,url_for,request,session,redirect
import warnings
import pickle
import requests
import time
import json
import numpy as np
import mysql.connector

warnings.filterwarnings('ignore')

app = Flask(__name__)


# ------------------------------------------------------------------------------


# Configure the MySQL database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2580'
app.config['MYSQL_DB'] = 'zoho'

# Configure the secret key for sessions
app.secret_key = 'your_secret_key'

def get_db():
    db_config = {
        "host": app.config['MYSQL_HOST'],
        "user": app.config['MYSQL_USER'],
        "password": app.config['MYSQL_PASSWORD'],
        "database": app.config['MYSQL_DB']
    }

    # Create a database connection
    db = mysql.connector.connect(**db_config)
    return db

# --------------------------------------------------------------------------------

@app.route('/')
def new():
    if 'token' in session:
        print(session)
        return render_template('predict.html', token=session['token'])
    else:
        return render_template('front.html')

@app.route('/signup')
def signup():

    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")

# ---------------------------------------------------------------------------------

@app.route('/signups', methods=['GET', 'POST'])
def signups():
    if request.method == 'POST':
        username = request.form['name']
        mail = request.form['mail']
        password = request.form['password']
        client_id = request.form['id']
        client_secret = request.form['secret']
        code = request.form['code']

        client_id = client_id
        client_secret = client_secret
        code = code 

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
            refresh_token = data['refresh_token']
            print(f'Access Token: {access_token}')
            print(f'Refresh Token:')
            print(f'Token Type: {token_type}')
            print(f'Expires in :{expires_in}')

            curs = get_db()
            cursor = curs.cursor()

            cursor.execute("INSERT INTO users (username, mail, passwords, token, cli, sec) VALUES (%s, %s, %s, %s, %s, %s)",
               (username, mail, password, refresh_token, client_id, client_secret))
            curs.commit()
            cursor.close()

            return redirect(url_for('login'))
        
        else:
            return render_template('signup.html')

@app.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'POST':
        username = request.form['mail']
        password = request.form['password']

        curs = get_db()
        cursor = curs.cursor()


        cursor.execute("SELECT * FROM users WHERE mail = %s AND passwords = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        print("user ========",user)

        if user:
            session['token'] = user[4]
            session['cli'] = user[5]
            session['sec'] = user[6]

            print(session['token'])
            return render_template("predict.html")
        else:
            return render_template('login.html', error='Invalid username or password')

# ---------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

# ---------------------------------------------------------------------------------

@app.route('/add')
def add():
    if 'token' in session:
        client_id = session['cli']
        client_secret = session['sec']
        refresh_token = session['token']

        token_url = 'https://accounts.zoho.com/oauth/v2/token'
        leads_url = 'https://www.zohoapis.com/crm/v2/Leads'
        
        lead_data = {
        "data": [
            {
                "Last_Name": "Jean",
                "First_Name": "Mathew",
                # Add other lead data here
                }
            ]
        }

        def refresh_access_token():
            payload = {
                'grant_type': 'refresh_token',
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token
            }

            response = requests.post(token_url, data=payload)
            return response.json()
        
        def insert_lead(access_token):
            headers = {
                'Authorization': f'Zoho-oauthtoken {access_token}'
            }
            response = requests.post(leads_url, json=lead_data, headers=headers)
            return response.json()

        
        try:
            access_token_response = refresh_access_token()
            if 'access_token' in access_token_response:
                access_token = access_token_response['access_token']
                lead_insert_response = insert_lead(access_token)
                return render_template("msg.html",msg = "1")
            else:
                return render_template("msg.html",msg = "0")
        except Exception as e:
            return render_template("msg.html",msg = "0")
    else:
        return redirect(url_for('login'))
        
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
def kl(access_token,dat):
    api_endpoint = 'https://www.zohoapis.com/crm/v2/Leads'

    lead_data = dat 

    #'{"data":[' + str(dat) + "]}"
    headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            # Send the second POST request to insert a lead
    res = requests.post(api_endpoint, json=lead_data, headers=headers)
            
    if res.status_code == 201:
        print("Lead inserted successfully.")
        lead_id = res.json()["data"][0]["details"]["id"]
        print(f"Lead ID: {lead_id}")
        return 1
    else:
        print(f"Error: {res.status_code} - {res.text}")
        print(dat)
        return 0

@app.route('/post2', methods=['POST'])
def post2():
    try:
        mail = request.form.get('mail')
        password = request.form.get('password')
        id = request.form.get('id')
        secret = request.form.get("secret")
        cd = request.form.get('code')
        print(dat)
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
        time.sleep(3)
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
            dat = json.loads(dat)
            m = kl(access_token,dat)
            if m == 1:
                return "yessssssssssss"
            else:
                m = 0
                return "nooooooooooooooooh ah ah "
        else:
            return "credential error"
    except Exception as e:
        print(f"Error: {str(e)}")
        print(dat)
        return "An error occurred"

# ------------------------------------------------------------------------------

@app.route("/predict",methods=["POST","GET"])
def predict():

    industry = request.form.get("industry")
    category = request.form.get("category")
    software = request.form.get("software")
    employee = request.form.get("employee")
    size = request.form.get("size")
    funding = request.form.get("funding")
    company = request.form.get("company")

    ind = industry.split(" ")[0]
    cat = category.split(" ")[0]
    sof = software.split(" ")[0]
    emp = employee.split(" ")[0]
    siz = size.split(" ")[0]
    fund = funding.split(" ")[0]


    with open('ml/model_crm.pkl', 'rb') as file:
        model = pickle.load(file)
        ar = np.array([[int(ind),int(cat),int(sof),int(emp),int(siz),int(fund)]])
    result = model.predict(ar)
    result = "YES" if result == 1 else "NO"


    industry = industry.split(" ")[1]
    category = category.split(" ")[1]
    software = software.split(" ")[1]
    employee = employee.split(" ")[1]
    size = size.split(" ")[1]
    funding = funding.split(" ")[1]

    data = [["Company Name",company],
            ["Industry Type",industry],
            ["Category",category],
            ["Software Type",software],
            ["No of Employee",employee],
            ["Size of Company",size],
            ["Funding type",funding],
            ["Ideal Customer",result],
            
            ]
    print("data ===== ",data[-1][-1])
    return render_template("result.html",data = data)

# -------------------------------------------------------------------------------
'''
@app.route("./predict/result/update",methods=["POST"])
def update():
'''




if __name__ == '__main__':
    app.run(debug=True)
