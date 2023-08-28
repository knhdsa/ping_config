import requests

url = "https://knhdsabot.knhdsa.repl.co"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Ping to {url} successful!")
        else:
            print(f"Failed to ping {url}. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}.")