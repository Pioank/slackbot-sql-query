import logging
logging.basicConfig(level=logging.DEBUG)

import os
import json

from slack import WebClient
from slack.errors import SlackApiError
from flask import Flask, request, make_response

from modal_view import modal_view
from communication import (send_message, send_csv_file)
from prepare_csv import prepare_csv

import pyodbc 
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as psql

app = Flask(__name__)

#slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token='slack_token')

@app.route("/interactive", methods=["POST"]) # This is for the interactive part of the APP where the form sends the payload (see /test)
def interactive():
  if "payload" in request.form:
    payload = json.loads(request.form["payload"]) # Obtain payload in JSON - the dialogue content
    values = payload["view"]["state"]["values"] # Navigate to the JSON and select the values
    
    marketingid = values["block_id1"]["a-id"]["value"] 
    channel_id = values["block_channel_id"]["channel_action"]["selected_option"]["value"] # Reading the channel_id from Payload store it as a string
    date_from = values["block_id2"]["action_id2"]["selected_date"] # Reading the date from from Payload store it as a string
    date_to = values["block_id3"]["action_id3"]["selected_date"] 
    country = values["block_id4"]["action_id4"]["selected_option"]["value"] 
    markchan = values["block_checkboxes"]["checkboxes_ation"]["selected_options"]
    
  
    values=list()
    for i in markchan:
      val = {key: i[key] for key in i.keys() & {'value'}} 
      val = list(val.values())
      val = val[0]
      values.append(val)
    
    uno = prepare_csv(date_from, date_to, country, values, marketingid)    
    send_message(client, channel_id, date_from) #From the communications.py
    send_csv_file(client, channel_id, uno) #From the communications.py
    
    
  return make_response("", 200)  

@app.route("/test", methods=["POST"]) # This is running when user uses slash /fu command and serves the form
def slack_app():
  try:
    trigger_id = request.form['trigger_id']
    api_response = client.views_open(
      trigger_id=trigger_id,
      view=modal_view(request.form["channel_id"]) # Calls the modal_view.py and passes the channel_id
    )
    return make_response("", 200)
  except SlackApiError as e:
    code = e.response["error"]
    return make_response(f"Failed to open a modal due to {code}", 200)

if __name__ == "__main__":
  # export SLACK_API_TOKEN=xoxb-***
  # export FLASK_ENV=development
  # python3 app.py
  app.run()
