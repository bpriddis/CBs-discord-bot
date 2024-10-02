# ocr_simulator.py
import random
from datetime import datetime, timedelta

def simulate_ocr(image_url):
    """
    Simulate OCR by returning predefined data for testing purposes.
    In a real implementation, this function would process the image using an OCR library.
    """
    maps = ["Trap", "Mountain Range", "Sleeping Giant", "North", "Tears of the Desert"]
    clan_tags = ["ABC", "XYZ", "123", "WOW", "PRO"]
    clan_names = ["AlphaBravo", "XRaYZulu", "OneTwoThree", "WorldOfWarships", "ProfessionalGamers"]
    
    return {
        "map": random.choice(maps),
        "clan_tag": random.choice(clan_tags),
        "clan_name": random.choice(clan_names),
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(0, 60))).strftime("%d.%m.%y %H:%M")
    }