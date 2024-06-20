# import asyncio

# async def fetch_data():
#     print('start fetching')
#     await asyncio.sleep(2)
#     print('done fetching')
#     return{'data': 1}

# async def print_numbers():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(0.25)

# async def main():
#     task1 = asyncio.create_task(fetch_data())
#     task2 = asyncio.create_task(print_numbers())
#     value = await task1
#     print(value)
#     await task2

# asyncio.run(main())    

import asyncio

async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")
    
async def print_numbers():
     for i in range(10):
         print(i)
         await asyncio.sleep(0.25) 

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5),
        delayed_hi(3),
        print_numbers(),
    )

asyncio.run(main())
