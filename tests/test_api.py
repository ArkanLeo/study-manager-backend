import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_full_flow():
    email = f"ana-{uuid.uuid4().hex[:8]}@example.com"
    create_user = client.post("/users", json={"name": "Ana", "email": email})
    assert create_user.status_code == 201
    user_id = create_user.json()["data"]["id"]

    create_course = client.post(
        "/courses",
        json={"title": "Python", "description": "Curso completo", "workload": 20},
    )
    assert create_course.status_code == 201
    course_id = create_course.json()["data"]["id"]

    enrollment = client.post("/enrollments", json={"user_id": user_id, "course_id": course_id})
    assert enrollment.status_code == 201

    duplicate = client.post("/enrollments", json={"user_id": user_id, "course_id": course_id})
    assert duplicate.status_code == 409

    user_courses = client.get(f"/users/{user_id}/courses")
    assert user_courses.status_code == 200
    assert len(user_courses.json()["data"]["courses"]) == 1
