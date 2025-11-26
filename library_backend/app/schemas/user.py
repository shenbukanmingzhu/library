from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def username_len(cls, v):
        if not 3 <= len(v) <= 20:
            raise ValueError('用户名必须3-20位')
        return v

    @field_validator('password')
    def password_len(cls, v):
        if len(v) < 6:
            raise ValueError('密码至少6位')
        return v