"""
Send message from file to slack channel.
TODO: move constants to config file.

Example:
    ```
    tfcaju % python scripts/post_to_slack.py $PWD/tmp/slack_msg.txt
    ```
"""
import sys
from slack_sdk import WebClient

from slack_sdk.errors import SlackApiError

SLACK_BEARER = "xoxb-"
SLACK_CHANNEL = "qa-test-runs"

client = WebClient(token=SLACK_BEARER)

print('Reading file to send:', sys.argv[1])
with open(sys.argv[1], 'r') as file:
    msg = file.read()

client.chat_postMessage(channel="#" + SLACK_CHANNEL, text=msg)
