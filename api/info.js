from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Config
CSRF_TOKEN = "fn7T1QBZRXceAU0LsP9niCAPvWZjuF8S"
DEV_NAME = "AKASHHACKER"

@app.route('/')
def home():
    return f"""
    <html>
        <head><title>{DEV_NAME} API</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1 style="color: #E1306C;">Instagram Scraper API</h1>
            <p>Developed by: <b>{DEV_NAME}</b></p>
            <hr>
            <p>Usage: <code>/api/insta?u=USERNAME</code></p>
        </body>
    </html>
    """

@app.route('/api/insta', methods=['GET'])
def get_insta_data():
    username = request.args.get('u')
    
    if not username:
        return jsonify({
            "status": "error",
            "developer": DEV_NAME,
            "message": "Username missing! Use ?u=username"
        }), 400
    
    if "@" in username:
        username = username.split("@")[0]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'x-csrftoken': CSRF_TOKEN,
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
        'Referer': f'https://www.instagram.com/{username}/'
    }

    try:
        api_url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
        response = requests.get(api_url, headers=headers)
        
        if response.status_code != 200:
            return jsonify({
                "status": "error",
                "developer": DEV_NAME,
                "message": "Instagram Blocked Request or User Not Found"
            }), response.status_code
            
        data = response.json()
        
        if 'data' in data and data['data']['user']:
            user_info = data['data']['user']
            # Yahan response mein aapka naam jayega
            return jsonify({
                "status": "success",
                "developer": DEV_NAME,
                "data": user_info
            })
        else:
            return jsonify({
                "status": "error", 
                "developer": DEV_NAME,
                "message": "User not found"
            }), 404

    except Exception as e:
        return jsonify({
            "status": "error", 
            "developer": DEV_NAME, 
            "message": str(e)
        }), 500

def handler(event, context):
    return app(event, context)
