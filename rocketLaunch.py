import requests
import json

response = requests.get("https://fdo.rocketlaunch.live/json/launches/next/5")
r = json.loads(response.text)

def get1(r):
    return f'Launch 1:\nVehicle Name: {r["result"][0]["name"]}\nProvider: {r["result"][0]["provider"]["name"]}\nVehicle: {r["result"][0]["vehicle"]["name"]}\nLauch Pad: {r["result"][0]["pad"]["name"]}\nLaunch Description: {r["result"][0]["launch_description"]}'

def get2(r):
    return f'Launch 2:\nVehicle Name: {r["result"][1]["name"]}\nProvider: {r["result"][1]["provider"]["name"]}\nVehicle: {r["result"][1]["vehicle"]["name"]}\nLauch Pad: {r["result"][1]["pad"]["name"]}\nLaunch Description: {r["result"][1]["launch_description"]}'

def get3(r):
    return f'Launch 3:\nVehicle Name: {r["result"][2]["name"]}\nProvider: {r["result"][2]["provider"]["name"]}\nVehicle: {r["result"][2]["vehicle"]["name"]}\nLauch Pad: {r["result"][2]["pad"]["name"]}\nLaunch Description: {r["result"][2]["launch_description"]}'

def get4(r):
    return f'Launch 4:\nVehicle Name: {r["result"][3]["name"]}\nProvider: {r["result"][3]["provider"]["name"]}\nVehicle: {r["result"][3]["vehicle"]["name"]}\nLauch Pad: {r["result"][3]["pad"]["name"]}\nLaunch Description: {r["result"][3]["launch_description"]}'

def get5(r):
    return f'Launch 5:\nVehicle Name: {r["result"][4]["name"]}\nProvider: {r["result"][4]["provider"]["name"]}\nVehicle: {r["result"][4]["vehicle"]["name"]}\nLauch Pad: {r["result"][4]["pad"]["name"]}\nLaunch Description: {r["result"][4]["launch_description"]}'


print(f"{get1(r)}\n\n{get2(r)}\n\n{get3(r)}\n\n{get4(r)}\n\n{get5(r)}\nAll data from RocketLaunch.live")
