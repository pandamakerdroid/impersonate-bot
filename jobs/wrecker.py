from telethon.sync import events
from utils.wrecking_greeting import jibbrish1
import toml

config = toml.load("config.toml")


@events.register(events.NewMessage(pattern="(?i).*"))
async def handle_wreck_group(event):
    if (
        hasattr(event.message, "_chat_peer")
        and hasattr(event.message._chat_peer, "channel_id")
        and event.message._chat_peer.channel_id
        in config["targets_wreck_groups"].values()
    ):
        print(f"keywords triggered by: {str(event.message._chat_peer.channel_id)}")
        await event.reply(jibbrish1())


@events.register(events.NewMessage(pattern="(?i).*"))
async def handle_wreck_person(event):
    if (
        hasattr(event.message, "user_id")
        and event.message.user_id in config["targets_wreck_person"].values()
    ):
        print(f"keywords triggered by: {str(event.message.user_id)}")
        await event.reply(jibbrish1())
