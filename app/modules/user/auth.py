from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from db.retrieve import retrieve

security = HTTPBasic()

from modules.user.model import UserModel

def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security)
) -> dict[str, Any]:
    username = credentials.username
    password = credentials.password
    
    try:
        _, _, _, users = retrieve(
            table=UserModel.get_table_name(),
            single=True,
            username=username,
            password_hash=password
        )
        
        return users[0]
    except HTTPException as e:
        try:
            _, _, _, users = retrieve(
                table=UserModel.get_table_name(),
                single=True,
                email=username,
                password_hash=password
            )
            
            return users[0]
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )