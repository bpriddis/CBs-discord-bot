# error_handler.py
import csv
from datetime import datetime

async def log_error(error, message):
    """Log errors to errors.csv and send an error message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_type = type(error).__name__
    error_description = str(error)

    # Log to errors.csv
    with open('errors.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, error_type, error_description, message.jump_url])

    # Send error message
    error_message = f"Error processing message: {message.jump_url}\nPlease check the format and attachments."
    await message.channel.send(error_message, delete_after=30)