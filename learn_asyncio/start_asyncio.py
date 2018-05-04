import asyncio


async def foo():
    print('0Running in foo')
    await asyncio.sleep(0)
    print('1Explicit context switch to foo again')


async def bar():
    print('2Explicit context to bar')
    await asyncio.sleep(0)
    print('3Implicit context switch back to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()