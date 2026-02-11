from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api')
def get_info():
    username = request.args.get('username', '1sortex')
    url = f"https://isal.isalhackerdeveloper.workers.dev/info?username={username}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Aapka Branding
        data['developer'] = "AKASHHACKER"
        
        return jsonify(data)
    except:
        return jsonify({"error": "API Down", "developer": "AKASHHACKER"}), 500

# Vercel ko is 'app' ki zaroorat hoti hai
