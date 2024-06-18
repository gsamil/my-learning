# Databricks notebook source
# MAGIC %md
# MAGIC ### Running a function in the background

# COMMAND ----------

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


# if __name__ == "__main__":
    # You can use this to run a function in the background
    # await_main()

# COMMAND ----------

await async_main()
print("Done!")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Running multiple functions in the background

# COMMAND ----------

import time
from asyncio import Task
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

THREADPOOL = ThreadPoolExecutor(5)


def update_lead(lead: str, new: str) -> str:
    return f"{lead}\n{new}"

def get_email_result(email: str) -> str:
    print(f"Getting email for {email}")
    time.sleep(1)
    print(f"Finished Email: {email}")
    return f"Email: {email}"

def get_linkedin_url(linkedin_url: str) -> str:
    print(f"Getting linkedin for {linkedin_url}")
    time.sleep(3)
    print(f"Finished Linkedin: {linkedin_url}")
    return f"Linkedin: {linkedin_url}"

async def _async_get_email_result(email: str) -> str:
    return await asyncio.get_event_loop().run_in_executor(
        THREADPOOL, lambda: get_email_result(email)
    )

async def _async_get_linkedin_url(linkedin_url: str) -> str:
    return await asyncio.get_event_loop().run_in_executor(
        THREADPOOL, lambda: get_linkedin_url(linkedin_url)
    )

async def async_run_multiple(
    email: Task[str | None] | None = None,
    linkedin_url: Task[str | None] | None = None,
) -> tuple[str, list[str]]:
    """
    Implementation of enrich_lead_information that allows for asynchronous data retrieval.
    Once all fields are retrieved, the function will terminate early.
    """
    start = time.monotonic()

    maybe_tasks = [
        email,
        linkedin_url,
    ]
    lead = "Lead Information:"  # Change this for your case
    early_termination_condition = False  # Change this for your case
    all_infos: list[str] = []
    early_termination: bool = False
    for task in maybe_tasks:
        if early_termination_condition:
            early_termination = True
            break
        if task and (new := await task):
            lead = update_lead(lead, new)
            all_infos.append(new)
    return lead, all_infos


async def _async_get_results(
    email: str,
    linkedin_url: str,
) -> str:
    result, all_infos = await async_run_multiple(
        email=asyncio.create_task(_async_get_email_result(email)),
        linkedin_url=asyncio.create_task(_async_get_linkedin_url(linkedin_url)),
    )

    return result


def await_get_results(email: str, linkedin_url: str) -> str:
    return asyncio.run(_async_get_results(email, linkedin_url))


if __name__ == "__main__":
    email = "abdullah@leadiq.com"
    linkedin_url = "https://www.linkedin.com/in/abdullah/"
    result = await_get_results(email, linkedin_url)
    print(result)
