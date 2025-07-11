import asyncio


async def main(x):
    print(x+1)
    return x
def callback(task: asyncio.Task):
    print('over', task.result())
coroutine = main(1)

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)
loop.close()