# World of Warships Clan Battles Results Tracker Bot

This Discord bot tracks and processes World of Warships Clan Battles results posted in a specific channel.

## Setup

1. Clone this repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following content:
   ```
   BOT_TOKEN=your_discord_bot_token
   CHANNEL_ID=your_channel_id
   ```
4. Update the `config.ini` file if needed.

## Usage

Run the bot:
```
python main.py
```

Commands (Admin only):
- `/process_history`: Process all channel messages, avoiding duplicates.
- `/process_new`: Process new messages since last run.
- `/status`: Confirm bot is online and display version number.

## File Structure

- `main.py`: Main bot logic
- `ocr_simulator.py`: Simulates OCR functionality
- `data_processor.py`: Processes and validates data
- `error_handler.py`: Handles and logs errors
- `config.ini`: Configuration file
- `requirements.txt`: List of required packages
- `clan_battles_results.csv`: Output file for processed data
- `errors.csv`: Log file for errors

## Testing

Run unit tests:
```
python -m unittest discover tests
```

## Maintenance

- Regularly backup the `clan_battles_results.csv` file.
- Monitor the `errors.csv` file for any recurring issues.
- Update the bot token if needed in the `.env` file.