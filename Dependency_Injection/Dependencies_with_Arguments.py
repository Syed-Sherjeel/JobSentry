from fastapi import FastAPI, status, Depends, HTTPException

app = FastAPI(title="Dependency InJection")
blogs = {
    "1": "FASTAPI Prereq",
    "2": "FASTAPI core",
    "3": "Building Webapp with FastAPI"
}

users = {
    "8": "oumpa",
    "9": "lumpa"
}


class GetObjectOr404:
    def __init__(self, source):
        self.source = source

    def __call__(self, id: str):
        output = self.source.get(id)
        if not output:
            raise HTTPException(detail=f"Object with id:{id} not found", status_code=status.HTTP_404_NOT_FOUND)
        return output


blog_dependency = GetObjectOr404(blogs)


@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name


user_dependency = GetObjectOr404(users)


@app.get("/user/{id}")
def get_user(user_name: str = Depends(user_dependency)):
    return user_name
