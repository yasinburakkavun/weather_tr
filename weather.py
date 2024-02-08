import requests

def hava_durumu(api_key, sehir):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200:
            main = data['main']
            temperature = main['temp'] - 273.15  # Kelvin'den Celsius'a çevirme
            description = data['weather'][0]['description']
            
            print(f"{sehir} için Hava Durumu:")
            print(f"Sıcaklık: {temperature:.2f} °C")
            print(f"Açıklama: {description}")
        else:
            print(f"Hata kodu: {response.status_code}")
            print(data['message'])
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # API anahtarınızı ve sorgulamak istediğiniz şehiri girin
    api_key = "8ee0396d4b60144b5b58a9c737428cec"
    sehir = input("Hava durumunu sorgulamak istediğiniz şehri girin: ")
    
    hava_durumu(api_key, sehir)

