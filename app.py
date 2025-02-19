import datetime
import os
import subprocess
from flask import Flask
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get current server time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

# Run 'top' command and get output
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    # Create HTML response
    response = f"""
    <html>
    <head><title>System Monitor</title></head>
    <body>
        <h3>Name: Anushka Patil</h3>
        <h3>User: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)