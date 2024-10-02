# data_processor.py
import csv
from datetime import datetime
import re

def process_message_data(message, ocr_data):
    """Process and validate data from the message and OCR results."""
    content = re.sub(r'<[^>]+>', '', message.content)  # Remove emojis
    result, enemy, rating = re.match(r'(\w+)\s+vs\s+(\w+)\s*\((\w+)\)', content).groups()

    # Convert timestamp
    timestamp = datetime.strptime(ocr_data['timestamp'], "%d.%m.%y %H:%M")
    formatted_timestamp = timestamp.strftime("%m/%d/%y %H:%M")

    return {
        "Result": result,
        "Enemy": enemy,
        "Rating": rating,
        "Timestamp": formatted_timestamp,
        "Map": ocr_data['map'],
        "Clan Tag": ocr_data['clan_tag'],
        "Clan Name": ocr_data['clan_name'] if ocr_data['clan_name'].isascii() else ocr_data['clan_tag'],
        "Message ID": str(message.id)
    }

def append_to_csv(data):
    """Append processed data to the CSV file."""
    filename = 'clan_battles_results.csv'
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ["Result", "Enemy", "Rating", "Timestamp", "Map", "Clan Tag", "Clan Name", "Message ID"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)