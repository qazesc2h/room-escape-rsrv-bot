from SlackAPI import SlackAPI
from os import environ

slack = SlackAPI(environ['OAUTH_TOKEN'])

channel_name = "bot-alarm"
query = "!"
text = "test"

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)
slack.post_thread_message(channel_id, message_ts, text)