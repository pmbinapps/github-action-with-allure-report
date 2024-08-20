set -x
SLACK_BEARER="xoxb-"
MSG="TF: message from testframework"
CHANNEL="qa-test-runs"

MSG=$(<./tmp/slack_msg.txt)

echo "Msg to SEND:" $MSG
curl -d "text=$MSG" -d "channel=$CHANNEL" -H "Authorization: Bearer $SLACK_BEARER" -X POST https://slack.com/api/chat.postMessage