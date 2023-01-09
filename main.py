from fastapi import FastAPI
from Routes.user import user
app = FastAPI(
    title= "Prueba CRUD",
    description= "CRUD FASTAPI",
    openapi_tags=[{
        "name": "users",
        "descripcion": "users Route"
    }
    ]

)

app.include_router(user)


