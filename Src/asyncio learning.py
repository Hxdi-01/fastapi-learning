import asyncio

async def say_hello():
    print ("Hello...")
    await asyncio.sleep(2)  # pause for 2 seconds, let others run
    print ("...World!")
# This is like a person saying "Hello", waiting 2 seconds, then saying "World!".
#asyncio.run(say_hello())

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main ():
    await asyncio.gather(task1(), task2())
asyncio.run(main())

# asyncio with httpx for calling APIs
import asyncio
import httpx

async def fetch_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(data['current_weather'])
asyncio.run(fetch_weather(25, 68))