#!/bin/bash

API_KEY="YOUR_API_KEY"
CITY=$1

# API'yi çağır ve veriyi al
response=$(curl -s "http://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_KEY")

# Durum kodunu kontrol et
status_code=$(echo "$response" | jq -r '.cod')

if [ "$status_code" == "200" ]; then
    temperature_kelvin=$(echo "$response" | jq -r '.main.temp')
    temperature_celsius=$(awk "BEGIN {print $temperature_kelvin - 273.15}")
    description=$(echo "$response" | jq -r '.weather[0].description')

    echo "$CITY için Hava Durumu:"
    echo "Sıcaklık: $temperature_celsius °C"
    echo "Açıklama: $description"
else
    message=$(echo "$response" | jq -r '.message')
    echo "Hata kodu: $status_code"
    echo "Hata mesajı: $message"
fi

