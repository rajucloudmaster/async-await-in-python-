import asyncio

async def main():
    print('tim')
    task= asyncio.create_task(foo('ggpd')) #@ creates seperate task independent
    await asyncio.sleep(1)
    # await task
    print('finihsied')  #calculate time

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())
