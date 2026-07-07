import os
import lmstudio as lms
from flask import Flask, jsonify

app = Flask(__name__)

# Fetch the host endpoint from Render environment variables
LM_STUDIO_HOST = os.getenv("LM_STUDIO_HOST", "http://localhost:1234/v1")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Point the client to your external hosting endpoint
        client = lms.Client(base_url=LM_STUDIO_HOST)
        
        # Example using a common open-source model string identifier
        model = client.llm("qwen3-4b") 
        result = model.respond("Reply with: 'Hello from Render!'")
        
        return jsonify({"response": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Render binds web services to port 10000 by default
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
