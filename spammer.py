from discord_webhook import DiscordWebhook, DiscordEmbed
import time

# Change empty fields
WEBHOOK_URL = ''
MESSAGETITLE = ''
DESCRIPTION = ''
COLOR = 242424
PICTUREURL = ''

# Optionally delay in seconds (1 ms = 0.001)
# Delay of 3 seconds is working best
DELAY = 3

# DO NOT TOUCH THIS
while True:
    webhook = DiscordWebhook(url=WEBHOOK_URL)

    embed = DiscordEmbed(title=MESSAGETITLE, description=DESCRIPTION, color=COLOR)
    embed.set_image(url=PICTUREURL)

    webhook.add_embed(embed)

    response = webhook.execute()

    print(response)

    time.sleep(DELAY)