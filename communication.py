from slack.errors import SlackApiError
import pandas as pd
from pandas import DataFrame

def send_message(client, channel_id, date_from):
  try:
      response = client.chat_postMessage(
        channel=channel_id,
        text="This is your data file from: " + date_from,
      )
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

def send_csv_file(client, channel_id, pandasdf): #pandasdf is the data that will be passed from app_slack_client.py
  try:
      response1 = client.files_upload(
            channels=channel_id,
            content=pandasdf.to_csv(index=False), # you can put here text with csv data
            # file='data.csv', # or use prepared file with prepare_csv function
            title='hello.csv',
            filetype='csv'
      )
  except SlackApiError as e:
    assert e.response["error"]
