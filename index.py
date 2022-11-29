import os
from SlackAPI import SlackAPI

token = os.getenv('OAUTH_TOKEN')

if token is not None:
  slack = SlackAPI(token)

  channel_name = "bot-alarm"
  query = "!"
  text = "test"

  channel_id = slack.get_channel_id(channel_name)
  message_ts = slack.get_message_ts(channel_id, query)
  slack.post_thread_message(channel_id, message_ts, text)