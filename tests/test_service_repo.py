from calidad import InMemoryRepository, UserService
import pytest

def test_service_and_repository_flow():
    repo = InMemoryRepository(name="RepoMem", owner="QA")
    service = UserService(name="Svc", owner="QA", repo=repo)
    repo.validate()
    service.validate()
    service.register_user("u1", {"email": "ana@example.com"})
    assert service.get_user("u1")["email"] == "ana@example.com"

def test_service_requires_repo():
    with pytest.raises(ValueError):
        UserService(name="Svc", owner="QA", repo=None).validate()
