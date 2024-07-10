# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare ingredients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)  # pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():
    print("eggs: prepare ingredients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  # pause, another tasks can be run
    print("eggs: ready")

async def main():
    start = time()
    await asyncio.gather(make_coffee(), fry_eggs())
    print(f"breakfast is ready in {time() - start:.2f} min")

asyncio.run(main())  # run top-level function concurrently
