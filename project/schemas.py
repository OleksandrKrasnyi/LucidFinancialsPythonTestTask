from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    """Schema for user creation"""
    email: EmailStr
    password: str

    @field_validator('password')
    def password_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str

class PostCreate(BaseModel):
    """Schema for post creation"""
    text: str

    @field_validator('text')
    def validate_size(cls, v):
        if len(v.encode('utf-8')) > 1048576:  # 1MB in bytes
            raise ValueError('Post size exceeds 1MB limit')
        return v

class PostResponse(BaseModel):
    """Schema for post response"""
    id: int
    text: str

    class Config:
        from_attributes = True