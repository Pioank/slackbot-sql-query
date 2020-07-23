def input_field(block_id, label, action_id):
  return {
            "type": "input",
            "block_id": block_id,
            "label": {
              "type": "plain_text",
              "text": label,
            },
            "element": {
              "action_id": action_id,
              "type": "plain_text_input",
            }
          }

def datepicker_field(block_id, label, action_id):
  return {
            "type": "input",
            "block_id": block_id,
            "label": {
              "type": "plain_text",
              "text": label,
            },
            "element": {
              "action_id": action_id,
              "type": "datepicker",
            }
          }

def options_field(block_id, label, action_id, options):
  return {
            "type": "input",
            "block_id": block_id,
            "label": {
              "text": label,
              "type": "plain_text"
            },
            "element": {
              "action_id": action_id,
              "type": "static_select",
              "placeholder": {
                "text": "Select the country",
                "type": "plain_text"
              },
              "options": options
            }
          }

def checkboxes_field(block_id, label, action_id, options):
  return {
            "type": "input",
            "block_id": block_id,
            "label": {
              "text": label,
              "type": "plain_text"
            },
            "element": {
              "action_id": action_id,
              "type": "checkboxes",
              "options": options
            }
          }
