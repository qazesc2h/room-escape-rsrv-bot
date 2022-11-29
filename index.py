from SlackAPI import SlackAPI

OAUTH_TOKEN = 'xoxb-4431164721781-4434055825491-Vc3y99FSGAEwUw6MHI9tqk3l'

slack = SlackAPI(OAUTH_TOKEN)

channel_name = "bot-alarm"
query = "!"
text = "test"

channel_id = slack.get_channel_id(channel_name)
message_ts = slack.get_message_ts(channel_id, query)
slack.post_thread_message(channel_id, message_ts, text)