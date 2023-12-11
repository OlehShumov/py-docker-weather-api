import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={"key": API_KEY, "q": CITY}
    ).json()
    print(
        f"Weather in {response['location']['name']}, "
        f"{response['location']['country']} "
        f"{response['location']['localtime']}:\n"
        f"Temperature: {response['current']['temp_c']} Celsius,\n"
        f"Weather condition: {response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
