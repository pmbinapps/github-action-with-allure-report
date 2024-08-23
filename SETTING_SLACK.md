# Setting Up Slack Webhooks

This guide provides step-by-step instructions on how to set up Slack webhooks to send messages directly to a Slack channel using incoming webhooks. For more detailed guidance, you can refer to this [YouTube video tutorial](https://youtu.be/6NJuntZSJVA).

## Check as below


```bash
curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, Slack!"}' YOUR_WEBHOOK_URL



curl -X POST -H 'Content-type: application/json' --data '{
    "text": "Hello, Slack!",
    "username": "MyBot",
    "icon_emoji": ":robot_face:",
    "attachments": [
        {
            "text": "This is an attachment",
            "color": "#36a64f"
        }
    ]
```


### Use in github actions like
For more details, you can watch this YouTube video tutorial which provides a comprehensive walkthrough of the steps outlined above.
}' YOUR_WEBHOOK_URL


```on: [push]

jobs:
  new_push_job:
    runs-on: ubuntu-latest
    name: New push to repo
    steps:
    - name: Send GitHub trigger payload to Slack Workflow Builder
      id: slack
      uses: slackapi/slack-github-action@v1.26.0
      with:
        payload: |
          {
            "text": "Danny Torrence left a 1 star review for your property.",
            "blocks": [
              {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "Danny Torrence left the following review for your property:"
                }
              },
              {
                "type": "section",
                "block_id": "section567",
                "text": {
                  "type": "mrkdwn",
                  "text": "<https://example.com|Overlook Hotel> \\n :star: \\n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
                },
                "accessory": {
                  "type": "image",
                  "image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
                  "alt_text": "Haunted hotel image"
                }
              },
              {
                "type": "section",
                "block_id": "section789",
                "fields": [
                  {
                    "type": "mrkdwn",
                    "text": "*Average Rating*\\n1.0"
                  }
                ]
              }
            ]
          }
      env:
        SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
```
#### Result 

![image](https://github.com/user-attachments/assets/892a1cb1-c592-431d-8852-784542a30c46)
