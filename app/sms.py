from urllib.parse import urlencode
from .settings import API_KEY, URL, SHORT_CODE
import requests
import aiohttp
import httpx
import asyncio
from urllib.parse import urlencode
from .utils import all_users


async def send_sms(phone: str, message: str):
    data = urlencode({
        "username": 'sandbox',
        "to": phone,
        "message": message,
        "from": SHORT_CODE
    })

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "apiKey": API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(URL, data=data, headers=headers)

        if response.status_code != 201:
            print(f"Error sending SMS: {response.text}")
            return False

        print("SMS sent successfully")
        return True


async def send_sms_to_all_users(message: str):
    tasks = []
    async with httpx.AsyncClient() as client:
        for user in all_users():
            data = urlencode({
                "username": 'sandbox',
                "to": user.phone,
                "message": message,
                "from": SHORT_CODE
            })

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "apiKey": API_KEY
            }

            task = asyncio.create_task(
                client.post(URL, data=data, headers=headers))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        for i, response in enumerate(responses):
            if response.status_code == 201:
                print(
                    f"SMS sent to user {i} ({all_users()[i].phone}) successfully")
            else:
                print(
                    f"Error sending SMS to user {i} ({all_users()[i].phone}): {response.text}")
