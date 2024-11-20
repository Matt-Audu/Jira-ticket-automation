from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json
import os

# Creating a flask application instance
app = Flask(__name__)

@app.route("/createjira", methods=['POST']) # A decorator  
def create_jira():
    url = "https://simplymailmatthew7.atlassian.net/rest/api/3/issue"

    API_TOKEN = os.getenv("JiraApi")

    auth = HTTPBasicAuth("simplymailmatthew7@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first Jira Ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10003"
        },
        "project": {
        "key": "SCRUM"
        },
        "summary": "Jira ticket for python project",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4252)