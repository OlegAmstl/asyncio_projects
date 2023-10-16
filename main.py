import asyncio


async def my_coroutine() -> None:
    print('Hello, World!')


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(3)
coroutine_result = coroutine_add_one(3)

print(f'Результат равен {function_result}, его тип {type(function_result)}')
# print(f'Результат равен {coroutine_result}, его тип {type(coroutine_result)}')


result = asyncio.run(coroutine_add_one(3))
print(result)
