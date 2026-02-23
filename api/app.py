from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Branding Configuration
DEV_HANDLE = "@Akash_Exploits_bot"

@app.route('/api')
def get_info():
    username = request.args.get('username', '1sortex')
    # Source API URL
    url = f"https://isal.isalhackerdeveloper.workers.dev/info?username={username}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # --- RE-BRANDING LOGIC ---
        # Purane credits ko overwrite karna
        data['developer'] = DEV_HANDLE
        data['owner'] = "@Akash Exploits"
        data['powered_by'] = "TITAN HYPERION V6"
        data['support'] = f"https://t.me/Akash_Exploits_bot"
        
        return jsonify(data)
    except Exception:
        # Error aane par bhi aapka hi branding dikhega
        return jsonify({
            "success": False,
            "error": "Upstream Service Down", 
            "developer": DEV_HANDLE,
            "support": "Contact @Akash_Exploits_bot"
        }), 500

# Vercel deployment ke liye
exposed_app = app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
