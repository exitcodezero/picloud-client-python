import os


PICLOUD_URL = os.getenv('PICLOUD_URL')
if PICLOUD_URL is None:
    raise ValueError("PICLOUD_URL environment variable is not exported")


PICLOUD_API_KEY = os.getenv('PICLOUD_API_KEY')
if PICLOUD_API_KEY is None:
    raise ValueError("PICLOUD_API_KEY environment variable is not exported")
