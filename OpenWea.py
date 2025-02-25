import requests

# Ваш API-ключ от OpenWeatherMap
API_KEY = 'your_api_key_here'

# Координаты (широта и долгота)
latitude = 45.0376  # Пример: Ставрополь
longitude = 41.9810  # Пример: Ставрополь

# URL для запроса погоды по координатам
url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()  # Получаем данные в формате JSON
    temperature = data['main']['temp']  # Температура в градусах Цельсия
    city = data['name']  # Название города
    print(f"Текущая температура в {city}: {temperature}°C")
else:
    print("Не удалось получить данные о погоде. Проверьте ваш API-ключ или координаты.")
