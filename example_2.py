import asyncio
from util import delay


async def add_one(n: int) -> int:
    return n + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello world'


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print('Пока я жду исполняется другой код')


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay
    # print(result)
    # message = await hello_world_message()
    # one_plus_one = await add_one(1)
    # print(one_plus_one)

asyncio.run(main())
