from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <head><title>DevOps with Ankita</title></head>
      <body style="background-color:#0f172a; color:#facc15; font-family:Arial, sans-serif; text-align:center; padding-top:100px;">
        <h1 style="font-size: 2.5rem;"><span style="color:#22d3ee;">Welcome to <span style="color:#a3e635;">DevOpswithAnkita</span></span></h1>
        <p style="font-size: 1.2rem; color:#e0f2fe;">
          Learn DevOps here 👉 
          <a href="https://github.com/DevOpswithAnkita" style="color:#f472b6; text-decoration:none;" target="_blank">
            github.com/DevOpswithAnkita
          </a>
        </p>
      </body>
    </html>
    """
@app.route('/api/docs')
def api_docs():
    return jsonify({
        "message": "Welcome to API Docs (protected with Basic Auth via NGINX)"
    })
