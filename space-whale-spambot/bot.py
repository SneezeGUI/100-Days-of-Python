import discord
from discord import Option
import random
import asyncio
from typing import Dict, Optional
import datetime
from dotenv import load_dotenv
import os
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Bot setup with all intents
bot = discord.Bot(intents=discord.Intents.all())

# Store message tasks and user message configurations
message_tasks: Dict[int, asyncio.Task] = {}
user_messages: Dict[int, str] = {}

# Load environment variables
load_dotenv()
bot_token = os.getenv('BOT_TOKEN')


async def dm_loop(user_id: int, message: str):
    """
    Asynchronous loop to send direct messages to a user at random intervals

    Args:
        user_id (int): The Discord user ID to send messages to
        message (str): The message content to send
    """
    while True:
        try:
            user = await bot.fetch_user(user_id)
            await user.send(message)

            delay = random.randint(5 * 60, 60 * 60)  # 5-60 minutes in seconds
            logger.info(f"Message sent to {user.name} (ID: {user_id}), next message in {delay / 60:.2f} minutes")
            await asyncio.sleep(delay)

        except discord.Forbidden:
            logger.error(f"Cannot send DM to user {user_id}. Missing permissions or DMs blocked.")
            if user_id in message_tasks:
                message_tasks[user_id].cancel()
                del message_tasks[user_id]
                del user_messages[user_id]
            break
        except discord.NotFound:
            logger.error(f"User {user_id} not found.")
            break
        except asyncio.CancelledError:
            logger.info(f"DM task cancelled for user {user_id}")
            break
        except Exception as e:
            logger.error(f"Unexpected error sending DM to {user_id}: {str(e)}")
            break


@bot.slash_command(name="start_dm", description="Start sending periodic DMs to a user")
@discord.commands.default_permissions(administrator=True)
async def start_dm(
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, "Select the user to DM", required=True),
        message: Option(str, "Message to send", required=True)
):
    try:
        # Check if command is used in a guild
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server!", ephemeral=True)
            return

        # Check if user already has active task
        if user.id in message_tasks:
            await ctx.respond("Already sending messages to this user!", ephemeral=True)
            return

        # Verify bot can DM the user
        try:
            await user.send("Bot DM test - Starting periodic messages.")
        except discord.Forbidden:
            await ctx.respond("Cannot send DMs to this user. They might have DMs disabled or blocked the bot.",
                              ephemeral=True)
            return
        except Exception as e:
            await ctx.respond(f"Error testing DM permissions: {str(e)}", ephemeral=True)
            return

        # Store message configuration and create task
        user_messages[user.id] = message
        task = asyncio.create_task(dm_loop(user.id, message))
        message_tasks[user.id] = task

        await ctx.respond(
            f"✅ Started sending periodic DMs to {user.mention}\nMessage: `{message}`",
            ephemeral=True
        )
        logger.info(f"Started DM task for user {user.id} ({user.name})")

    except Exception as e:
        logger.error(f"Error in start_dm command: {str(e)}")
        await ctx.respond("An unexpected error occurred. Please try again later.", ephemeral=True)

@bot.slash_command(name="stop_dm", description="Stop sending periodic DMs to a user")
@discord.commands.default_permissions(administrator=True)
async def stop_dm(
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, "Select the user to stop DMing", required=True)
):
    try:
        # Check if command is used in a guild
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server!", ephemeral=True)
            return

        if user.id not in message_tasks:
            await ctx.respond("No active DM task for this user!", ephemeral=True)
            return

        # Cancel the task and remove from storage
        message_tasks[user.id].cancel()
        del message_tasks[user.id]
        del user_messages[user.id]

        await ctx.respond(f"✅ Stopped sending DMs to {user.mention}", ephemeral=True)
        logger.info(f"Stopped DM task for user {user.id} ({user.name})")

    except Exception as e:
        logger.error(f"Error in stop_dm command: {str(e)}")
        await ctx.respond("An unexpected error occurred. Please try again later.", ephemeral=True)

@bot.slash_command(name="update_message", description="Update the message being sent to a user")
@discord.commands.default_permissions(administrator=True)
async def update_message(
        ctx: discord.ApplicationContext,
        user: Option(discord.Member, "Select the user", required=True),
        new_message: Option(str, "New message to send", required=True)
):
    try:
        # Check if command is used in a guild
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server!", ephemeral=True)
            return

        if user.id not in message_tasks:
            await ctx.respond("No active DM task for this user!", ephemeral=True)
            return

        # Update the message and restart the task
        user_messages[user.id] = new_message
        message_tasks[user.id].cancel()
        task = asyncio.create_task(dm_loop(user.id, new_message))
        message_tasks[user.id] = task

        await ctx.respond(
            f"✅ Updated message for {user.mention}\nNew message: `{new_message}`",
            ephemeral=True
        )
        logger.info(f"Updated message for user {user.id} ({user.name})")

    except Exception as e:
        logger.error(f"Error in update_message command: {str(e)}")
        await ctx.respond("An unexpected error occurred. Please try again later.", ephemeral=True)

@bot.slash_command(name="list_active", description="List all active DM tasks")
@discord.commands.default_permissions(administrator=True)
async def list_active(ctx: discord.ApplicationContext):
    try:
        # Check if command is used in a guild
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server!", ephemeral=True)
            return

        if not message_tasks:
            await ctx.respond("No active DM tasks", ephemeral=True)
            return

        response = "📝 **Active DM Tasks:**\n\n"
        for user_id, task in message_tasks.items():
            user = await bot.fetch_user(user_id)
            message = user_messages[user_id]
            response += f"👤 **User:** {user.name} ({user_id})\n💬 **Message:** `{message}`\n\n"

        await ctx.respond(response, ephemeral=True)
        logger.info(f"Listed active tasks for {ctx.author.name}")

    except Exception as e:
        logger.error(f"Error in list_active command: {str(e)}")
        await ctx.respond("An unexpected error occurred. Please try again later.", ephemeral=True)

@bot.event
async def on_ready():
    try:
        logger.info(f'Bot is ready! Logged in as {bot.user.name} (ID: {bot.user.id})')

        # Sync commands with proper error handling
        try:
            # For global commands
            commands = await bot.sync_commands()
            if commands is not None:
                logger.info(f"Successfully synced {len(commands)} global command(s)")
            else:
                logger.info("No commands were synced (returned None)")

            # Optional: For guild-specific commands, uncomment and modify as needed
            # test_guild_id = 123456789  # Replace with your test guild ID
            # guild = bot.get_guild(test_guild_id)
            # if guild:
            #     guild_commands = await bot.sync_commands(guild_id=test_guild_id)
            #     logger.info(f"Synced {len(guild_commands) if guild_commands else 0} commands to test guild")

        except discord.errors.Forbidden as e:
            logger.error(f"Failed to sync commands: Missing permissions - {str(e)}")
        except discord.errors.HTTPException as e:
            logger.error(f"Failed to sync commands: HTTP Exception - {str(e)}")
        except Exception as e:
            logger.error(f"Failed to sync commands: {str(e)}")

    except Exception as e:
        logger.error(f"Error in on_ready event: {str(e)}")



def run_bot():
    """Wrapper function to run the bot with proper error handling"""
    try:
        if not bot_token:
            raise ValueError("Bot token not found in environment variables")

        # Add startup message
        logger.info("Starting bot...")

        # Run the bot with error handling
        bot.run(bot_token, reconnect=True)

    except discord.LoginFailure:
        logger.critical("Failed to start bot: Invalid token")
    except discord.PrivilegedIntentsRequired:
        logger.critical(
            "Failed to start bot: Privileged intents are required but not enabled in Discord Developer Portal")
    except Exception as e:
        logger.critical(f"Failed to start bot: {str(e)}")
        raise


if __name__ == "__main__":
    # Setup basic configuration message
    logger.info("Initializing bot...")
    run_bot()

