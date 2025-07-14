import requests

def kelvin_to_celsius(kelvin_temp):
    return round(kelvin_temp - 273.15, 2)

def kelvin_to_fahrenheit(kelvin_temp):
    return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

def get_weather(city, units="C"):
    API_KEY = "785997b44ea51547d9ca40e5ff50162d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message', 'City not found')}")
            return

        temp_k = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()

        if units == "F":
            temperature = f"{kelvin_to_fahrenheit(temp_k)} °F"
        else:
            temperature = f"{kelvin_to_celsius(temp_k)} °C"

        print(f"\n📍 Weather in {data['name']}:")
        print(f"🌡️ Temperature: {temperature}")
        print(f"🌤️ Condition: {description}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.RequestException as e:
        print("❌ Network error occurred:", e)

if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ").strip()
    unit = input("Choose temperature unit - C (Celsius) or F (Fahrenheit): ").strip().upper()

    if unit not in ["C", "F"]:
        unit = "C"

    get_weather(city, unit)
