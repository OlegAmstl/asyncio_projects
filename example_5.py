import asyncio
from util import delay

async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(task, timeout=5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5 секунд, скоро она закончится!")
        result = await task
        print(result)


asyncio.run(main())