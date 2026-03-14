from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3

app = Flask(__name__)

# allow requests from the browser
CORS(app, resources={r"/*": {"origins": "*"}})

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

@app.route("/ask", methods=["POST"])
def ask_nova():
    user_question = request.json["question"]

    response = bedrock.converse(
        modelId="us.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": user_question}]
            }
        ]
    )

    answer = response["output"]["message"]["content"][0]["text"]

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)