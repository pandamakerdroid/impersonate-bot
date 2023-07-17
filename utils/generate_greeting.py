import datetime

def generate_greeting():
    now = datetime.datetime.now()
    greeting = ''
    if now.hour < 18:
        greeting = "Bonjour, mes dames et messieurs! "
    elif now.hour >= 18:
        greeting = "Bonsoir, mes dames et messieurs! "
    return greeting