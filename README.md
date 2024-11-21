# Jira automation with Github using python flask application

This project focuses on using python to automate jira ticket creation with github webhooks. This is a Flask application for creating Jira tickets via a POST request to a `/createjira` endpoint. The application uses basic authentication and a Jira API token to authenticate requests. The application was hosted on an ec2 instance. Github Webhook sends a POST request to the server I.P address whenever there's a comment on an issue in that particular repository.

## Prerequisites
- Open a Jira account
- Install python
- Create a new github repository
- Ec2 instance
- flask
- Requests
- Python 3.x and higher

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Matt-Audu/Jira-ticket-automation.git
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install flask requests
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your Jira API token:
    ```sh
    export JiraApi=your_actual_jira_api_token
    ```

### Usage

1. **Run the Flask app**:
    ```sh
    flask-app.py
    ```

2. **Send a POST request to create a Jira ticket**:
    ```sh
    curl -X POST http://localhost:4252/createjira
    ```
3. **Deploy python app on ec2 instance**:
   ```
   Run the same process from beginning on your linux (Ubuntu) server.

### Integrate with github webhooks

- Navigate to the settings in your github repository.
- Create a webhook and select "Issue comment" as the trigger.
- Copy your server public dns I.P address with port 4252/createJira.
- Paste I.P address into your github webhook and save.

### Test the application

- Go over to "Issue" in your github repository
- Create a new issue and write a cooment.
