from fastapi import FastAPI
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: str | None
    

app = FastAPI()

@app.get("/home")
def get_home():
    return {"id": 1,
            "data": "home page"}
#
# def main():
#     print("main function is now")
#
#
# if __name__ == "__main__":
#     main()
#     print("this is for new branch")
