from fields import (input_field, datepicker_field, options_field, checkboxes_field)

def modal_view(channel_id): # I have to add channel id here to be posible to send message to bot channel
  return {
        "type": "modal",
        "callback_id": "modal-id",
        "title": {
          "type": "plain_text", #Takes only specific values such as plain_text check Slack API documentation
          "text": "UNO data request"
        },
        "submit": {
          "type": "plain_text", 
          "text": "Submit"
        },
        "close": {
          "type": "plain_text",
          "text": "Cancel"
        },
        "blocks": [
          options_field("block_channel_id", "Channel ID", "channel_action", [ { # this field was prepared bacause in request from dialog there is no channel id
                  "text": {
                    "type": "plain_text",
                    "text": "My channel ID"
                  },
                  "value": channel_id
                }]),
          input_field( "block_id1", "Provide a marketing ID (Campaign ID, Creative ID etc.)", "a-id"),
          datepicker_field("block_id2", "Date from", "action_id2"),
          datepicker_field("block_id3", "Date to", "action_id3"),
          options_field("block_id4", "Country", "action_id4", [
                {
                  "text": {
                    "type": "plain_text",
                    "text": "United Kindom" # Change to display different
                  },
                  "value": "uk" # Change to pass this value back 
                },
                {
                  "text": {
                    "type": "plain_text",
                    "text": "Spain"
                  },
                  "value": "es"
                },
                {
                  "text": {
                    "type": "plain_text",
                    "text": "Italy"
                  },
                  "value": "it"
                },
                {
                  "text": {
                    "type": "plain_text",
                    "text": "Rest of the World"
                  },
                  "value": "row"
                }
              ]),
          checkboxes_field("block_checkboxes", "Marketing_Channel", "checkboxes_ation", [
                    {
                        "value": "Affiliates",
                        "text": {
                            "type": "plain_text",
                            "text": "Affiliates"
                        }
                    },
                    {
                        "value": "Direct",
                        "text": {
                            "type": "plain_text",
                            "text": "Direct"
                        }
                    },
                    {
                        "value": "Media",
                        "text": {
                            "type": "plain_text",
                            "text": "Media"
                        }
                    },
                    {
                        "value": "Pay Per Click",
                        "text": {
                            "type": "plain_text",
                            "text": "Pay Per Click"
                        }
                    },
                    {
                        "value": "Programmatic",
                        "text": {
                            "type": "plain_text",
                            "text": "Programmatic"
                        }
                    },
                    {
                        "value": "Search Engine Optimisation",
                        "text": {
                            "type": "plain_text",
                            "text": "Search Engine Optimisation"
                        }
                    },
                    {
                        "value": "Social Media",
                        "text": {
                            "type": "plain_text",
                            "text": "Paid Social"
                        }
                    },
                ])
        ]
      }
      