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


if __name__ == "__main__":
    # You can use this to run a function in the background
    await_main()
