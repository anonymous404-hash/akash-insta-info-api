from flask import Flask, request, jsonify
import requests

# Yahan 'app' define karna zaroori hai
app = Flask(__name__)

CSRF_TOKEN = "fn7T1QBZRXceAU0LsP9niCAPvWZjuF8S"
DEV_NAME = "AKASHHACKER"

@app.route('/')
def home():
    return f"<h1>Instagram API by {DEV_NAME}</h1><p>Use /api/insta?u=username</p>"

@app.route('/api/insta')
def get_insta_data():
    username = request.args.get('u')
    if not username:
        return jsonify({"error": "Username missing", "developer": DEV_NAME}), 400
    
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
        data = response.json()
        
        if 'data' in data and data['data']['user']:
            return jsonify({
                "status": "success",
                "developer": DEV_NAME,
                "data": data['data']['user']
            })
        else:
            return jsonify({"error": "User not found", "developer": DEV_NAME}), 404

    except Exception as e:
        return jsonify({"error": str(e), "developer": DEV_NAME}), 500

# Ye line hata do (handler wali), iski zaroorat nahi hai naye setup mein
if __name__ == "__main__":
    app.run()
