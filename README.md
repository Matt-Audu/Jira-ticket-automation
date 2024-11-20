# Jira automation with Github using python flask application

This project focuses on using python to automate jira ticket creation with github webhooks. The python application was created using the flask framework and interacts with Jira API to create an issue on jira. The application was hosted on an ec2 instance.

Github Webhook sends a POST request to the server I.P address whenever there's a comment on an issue in that particular repository.

## Prerequisites
1. Open a Jira account
2. Install python
3. Create a new github repository
4. An ec2 instance