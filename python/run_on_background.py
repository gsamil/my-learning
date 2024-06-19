import time
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

THREADPOOL = ThreadPoolExecutor(5)


def main():
    print("Hello, World!")
    time.sleep(1)
    print("Goodbye, World!")


async def async_main() -> None:
    # Run main in the background, but don't wait for it
    asyncio.get_event_loop().run_in_executor(THREADPOOL, main)


def await_main() -> None:
    asyncio.run(async_main())
    print("Done!")


"""
# Running a function in the background

I didn't make this a jupyter notebook because jupyter has it's own running event loop
So just run `python run_on_background.py` to see the expected output:

```
Hello, World!
Done!
Goodbye, World!
```
"""
if __name__ == "__main__":
    await_main()