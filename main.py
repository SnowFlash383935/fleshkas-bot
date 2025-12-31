import os
import discohook

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
PUBLIC_KEY = os.environ["PUBLIC_KEY"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
APPLICATION_PASSWORD = os.environ["APPLICATION_PASSWORD"]

# Create client instance (use a different name to avoid conflict)
client = discohook.Client(
    application_id=APPLICATION_ID,
    public_key=PUBLIC_KEY,
    token=DISCORD_TOKEN,
    password=APPLICATION_PASSWORD,
    default_help_command=True,
)

# Error handlers (use 'client' instead of 'app')
@client.on_interaction_error()
async def interaction_error_handler(i: discohook.Interaction, err: Exception):
    user_response = "Some error occurred! Please contact the developer."
    if i.responded:
        await i.response.followup(user_response, ephemeral=True)
    else:
        await i.response.send(user_response, ephemeral=True)
    await client.send("12345678910", f"Error: {err}")

@client.on_error()
async def server_error_handler(_request, err: Exception):
    await client.send("12345678910", f"Error: {err}")

# Commands (use 'client.load')
@client.load
@discohook.command.slash()
async def ping(i: discohook.Interaction):
    """Ping the bot."""
    await i.response.send("Pong!")

@client.load
@discohook.command.user()
async def avatar(i: discohook.Interaction, user: discohook.User):
    embed = discohook.Embed()
    embed.set_image(img=user.avatar.url)
    await i.response.send(embed=embed)

@client.load
@discohook.command.message()
async def quote(i: discohook.Interaction, message: discohook.Message):
    embed = discohook.Embed()
    embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
    embed.description = message.content
    await i.response.send(embed=embed)

# Export the ASGI app for Vercel
app = client.app  # or try client.asgi_app if .app doesn't work
