# example of using an asyncio queue
from random import random
import asyncio
import time
 
 #couroutine to generate ework
start_time = time.perf_counter()
async def producer(queue):
    print('Producer: Running')
    #generate work
    for i in range(10):
        start_time = time.time()
        # generate a value
        value = 1
        # block to simulate worwk
        await asyncio.sleep(random())
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
end_time = time.perf_counter()
#coroutine to cosume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        #get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')

#entry point coroutine
async def main():
    # create the shard queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue),consumer(queue))

# start the asyncio program
if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{time.ctime()} - Done in {elapsed} seconds.")