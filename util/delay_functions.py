import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds} c')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течении {delay_seconds} с закончен')
    return delay_seconds
