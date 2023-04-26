import python_weather
import asyncio
import os
import sys 
import requests


if __name__ == "__main__":


	opc = 0

	while(opc == 0):
		print("What do you what to do?\n")
		print("1.Get the current weather\n")
		print("2.Get the elevation\n")
		print("3.Stop it!\n")

		opc = input()

		if(opc == 3):
			break

		if(9)

	laitud = ""
	longitude = "" 

	url = "https://api.open-meteo.com/v1/forecast?latitude="+latitud+"&longitude="+longitud+"&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

	response = requests.get(url)

	response_json = response.json()
	print(response_json)

