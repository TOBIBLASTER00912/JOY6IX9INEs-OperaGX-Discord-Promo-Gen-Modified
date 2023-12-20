import requests
import string
import random
import threading
import time
import ctypes
import os
import uuid

os.system('cls' if os.name == 'nt' else 'clear')

class counter:
    count = 0

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = time.strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

def gen():
    while True:
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }

        data = {
            "partnerUserId": str(uuid.uuid4())
        }

        try:
            response = requests.post(url, json=data, headers=headers, timeout=5)

            if response.status_code == 200:
                token = response.json().get('token')
                if token:
                    counter.count += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Opera Gx Promo Gen | Made With <3 By Joy & TOBIBLASTER0912"
                            f" | Generated : {counter.count}")
                    link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                    with open("promos.txt", "a") as f:
                        f.write(f"{link}\n")
                    print(f"{get_timestamp()} {green} Generated Promo Link : {link}")
            elif response.status_code == 429:
                print(f"{get_timestamp()} {yellow} You are being rate-limited! Waiting 1 Minute...")
                time.sleep(60)  # Wait for 5 seconds before trying again
            else:
                print(f"{get_timestamp()} {red} Request failed : {response.status_code}")
        except Exception as e:
            print(f"{get_timestamp()} {red} Request Failed : {e}")

def main():
    num_threads = int(input(f"{get_timestamp()} {blue} Enter Number Of Threads : "))
    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=gen)
        threads.append(thread)

    for thread in threads:
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
