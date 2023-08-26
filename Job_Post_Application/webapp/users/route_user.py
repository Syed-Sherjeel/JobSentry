from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends, responses, status

from db.session import get_db
from webapp.users.forms import UserCreateForm
from db.repository.users import CreateUser, create_new_user

router = APIRouter(include_in_schema=False)
template = Jinja2Templates(directory="templates")


@router.get("/register/")
def get_register_template(request: Request):
    return template.TemplateResponse("users/register.html", {"request": request})


@router.post("/register/")
async def register(request: Request, db: Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_form()
    if await form.validate_form():
        user = CreateUser(username=form.name, password=form.password, email=form.email)
        try:
            _ = create_new_user(user, db)
            return responses.RedirectResponse(
                "/login/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
            )
        except IntegrityError:
            form.__dict__.get("errors").append("Username or Email Already Exists")
            print(form.__dict__)
            return template.TemplateResponse("users/register.html", form.__dict__)

    return template.TemplateResponse("users/register.html", form.__dict__)
