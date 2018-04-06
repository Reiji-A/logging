import logging
logging.basicConfig()
logging.getLogger("urllib3").setLevel(level=logging.DEBUG)

# put in your code!
import requests
r = requests.get("https://google.com/")
