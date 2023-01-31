from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database


database = Database('postgresql://postgres:9785@localhost:5432/postgres')


class User(BaseModel):
    id: int
    name: str
    gender: str


app = FastAPI()

@app.get("/list")
async def user_list():
    await database.connect()
    query = """select * from users_test order by id"""
    results = await database.fetch_all(query=query)
    return results


@app.get("/gender/")
async def user_filter(gender: str, limit: int):
    await database.connect()
    query = f"""select * from users_test where gender = '{gender}' order by id limit {limit}"""
    result =  await database.fetch_all(query=query)
    return result


@app.post("/create/") 
async def user_create(param: User):
    await database.connect()
    query = """insert into users_test (id,name,gender) values (:id, :name,:gender)"""
    values = [{"id": param.id,"name": param.name, "gender": param.gender}]
    await database.execute_many(query=query, values=values)
    
    
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000)