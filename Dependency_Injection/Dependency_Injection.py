from fastapi import FastAPI, Depends

app = FastAPI(title="Simple app that insert data to db")

dev_db = ["Development db"]

def get_db_session():
    return dev_db

@app.get("/add-item/")
def insert_into_db(item:str, db=Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message": f"item added: {item}"}

