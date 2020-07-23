# slackbot-sql-query

Summary: A slack bot which collects your data query through a dialogue and returns a CSV. The data bot is obtaining the data from your SQL server.

Thechnical summary: This is a WebApplication written in Python 3.8 (Flask) and tested locally with Ngrok which forwards the local port to a public endpoint which can later be used in Slack

Requirements: 
1) Python 3
2) Slack account / workspace with Admin rights
3) Ability to deploy your app on the web (if not use Ngrok)
4) An SQL Server or MySQL

Slack setup:
1) Ad to your Bot Token Scopes: channels:read , chat:write, commands, files:write, im:write, users:read
2) Under the interactivity tab add your app end point in the request URL field (select a route of your app e.g. yourapp.com/intercative)
3) In the Slash commands tab create a new command (/command) which will trigger the dialogue 

Python files:
1) app_slack_client.py : Is the the main App .py which imports all other .py files in the folder. It contains all app routes and reads the JSON response of the dialogue
2) communication.py: It contains 2 defs, one sending a string message and the other uploads a CSV
3) fields.py: Fields are defs per element for the dialogue and represent the static structure for each element. This makes it easier for the developer to add more elements / fields with less coding effort and in a more structured way
4) modal_view.py: Contains a def with the static JSON structure as dictated from Slack for a modal / dialogue and calls the fields from fields.py
5) prepare_csv: Is processing the data input from the dialogue form, performing the SQL query and returning the data frame to the app_slack_client.py

Detailed App flow description:

The application is democratising the data sitting in your database with the wider organisation that is already familiar with Slack given that it is the "chat" app used within your organisation.

Users have access to the bot under the Slack apps and from there they can prompt the dialogue by writing the command /request and press enter

The dialogue (current state) requires to add the slack channel ID (still trying to figure out how to skip that) and the rest fields are filters in order to request specific data.

Filters in this app contain:
 1) Text input which is looked up across multiple columns
 2) Date pickers (from - to)
 3) Drop down for country selection
 4) Checkboxes for marketing channel selection
 
 Upon submission of the form a JSON with the values is being sent to a predefined endpoint of your app, where you extract them for further processing.
 
 The values captured are being processed and passed into an SQL query as variables.
 
 The SQL query output is converted to a pandas Dataframe that later is being converted to CSV (using still pandas) and returned to the Slack bot where the user can download it.
 
 
