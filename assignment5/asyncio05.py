from random import random
import asyncio

async def cook_menu(menu):
    if menu == 'rice':
        value = random() + 1
        await asyncio.sleep(value)
        print(f"Rice cooked in {value:.4f} seconds")
        await asyncio.sleep(1)
        print(f"Rice finished cooking")
        return value
    elif menu == 'noodle':
        value = random() + 1
        await asyncio.sleep(value)
        print(f"Noodle cooked in {value:.4f} seconds")
        await asyncio.sleep(1)
        print(f"Noodle finished cooking")
        return value
    elif menu == 'curry':
        value = random() + 1
        await asyncio.sleep(value)
        print(f"Curry cooked in {value:.4f} seconds")
        await asyncio.sleep(1)
        print(f"Curry finished cooking")
        return value

async def main():
    menues= ['rice', 'noodle', 'curry']

    # Create tasks for fastest to the lastest
    tasks = [asyncio.create_task(cook_menu(item), name=item) for item in menues]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f'Completed task: {len(done)}')
    first = done.pop()
    result = first.result()
    print(f'{first.get_name()} is completed in {result:.2f} seconds' )
    print(f'Uncompleted task: {len(pending)}')
asyncio.run(main())
