from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: dict | list | None


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    created_at: datetime


class CourseCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=5, max_length=500)
    workload: int = Field(gt=0)


class CourseUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=5, max_length=500)
    workload: int = Field(gt=0)


class CourseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    workload: int


class EnrollmentCreate(BaseModel):
    user_id: int = Field(gt=0)
    course_id: int = Field(gt=0)


class EnrollmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime
