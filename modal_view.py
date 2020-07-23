from fields import (input_field, datepicker_field, options_field, checkboxes_field)

def modal_view(channel_id): # I have to add channel id here to be posible to send message to bot channel
  return {
        "type": "modal",
        "callback_id": "modal-id",
        "title": {
          "type": "plain_text", #Takes only specific values such as plain_text check Slack API documentation
          "text": "Data request" #This is the caption visible on the modal
        },
        "submit": {
          "type": "plain_text", 
          "text": "Submit" #CTA text
        },
        "close": {
          "type": "plain_text",
          "text": "Cancel" #CTA text
        },
        "blocks": [
          options_field("block_channel_id", "Channel ID", "channel_action", [ { # this field was prepared bacause in request from dialog there is no channel id
                  "text": {
                    "type": "plain_text",
                    "text": "My channel ID"
                  },
                  "value": channel_id
                }]),
          input_field( "block_id1", "Provide a marketing ID (Campaign ID, Creative ID etc.)", "a-id"), #Def from the fields.py
          datepicker_field("block_id2", "Date from", "action_id2"),  #Def from the fields.py
          datepicker_field("block_id3", "Date to", "action_id3"),  #Def from the fields.py
          options_field("block_id4", "Country", "action_id4", [
                {
                  "text": {
                    "type": "plain_text",
                    "text": "United Kindom" # Change to display different
                  },
                  "value": "uk" # Change to pass this value back 
                } #You can add more options by extending the same JSON structure
              ]),
          checkboxes_field("block_checkboxes", "Marketing_Channel", "checkboxes_ation", [
                    {
                        "value": "Channel1",
                        "text": {
                            "type": "plain_text",
                            "text": "Channel1"
                        }
                    },
                    {
                        "value": "Channel2",
                        "text": {
                            "type": "plain_text",
                            "text": "Channel2"
                        }
                    },

                ])
        ]
      }
      
