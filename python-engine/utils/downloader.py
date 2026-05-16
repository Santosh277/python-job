import os
import uuid
import httpx



def download_resume(url):
    os.makedirs("temp",exist_ok=True)
    response = httpx.get(url)
    content_type = response.headers.get("content-type","")
    extension = "pdf"
    if "word" in content_type:
        extension = "docx"
    elif "pdf" in content_type:
        extension = "pdf"
    
    file_name = f"temp/{uuid.uuid4()}.{extension}"

    with open(file_name, "wb") as file:
        file.write(response.content)
    
    return file_name