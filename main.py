from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
title="FAST API LMS",
description="LMS for Managing Students and Courses.",
contact={
    "name": "M.Waqas",
    "email": "abdullahwaqas22@gmail.com"

},
license_info={
    "name": "Associate Software Engineer"
}

)

from api import users, sections, courses

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


