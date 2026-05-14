import os
import uuid
import httpx



def download_resume(url):

    extension = url.split(".")[-1].split("?")[0]

    file_name = f"temp/{uuid.uuid4()}.{extension}"

    response = httpx.get(url)

    with open(file_name, "wb") as file:
        file.write(response.content)

    return file_name