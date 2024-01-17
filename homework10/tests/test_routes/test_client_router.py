from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from routes.client_routes import client_router
from dependencies import get_client_repository
from models.client import Client
from datetime import datetime, date
from mockito import when, mock, verify

import json
import sys
import os

from services.abc_repository.abc_client_repository import ABCClientRepository

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="function")
def client_list() -> list[Client]:
    return [Client(client_id=i,
                   document=f'document{i}',
                   sur_name=f'sur_name_{i}',
                   first_name=f'first_name_{i}',
                   patronymic=f'patronymic_{i}',
                   birthday=date.today())
            for i in range(1, 4)]


@pytest.fixture(scope="function")
def mock_client_repository(client_list: list[Client]) -> ABCClientRepository:
    _mock_client_repository = mock(ABCClientRepository)
    return _mock_client_repository


@pytest.fixture(scope="function")
def app(mock_client_repository: ABCClientRepository) -> Generator[FastAPI, Any, None]:
    _app = FastAPI()
    _app.include_router(client_router)

    def _get_test_client_repository():
        return mock_client_repository

    _app.dependency_overrides[get_client_repository] = _get_test_client_repository

    yield _app


@pytest.fixture(scope="function")
def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    with TestClient(app) as client:
        yield client


def test_get_all_client(client, mock_client_repository, client_list):
    when(mock_client_repository).get_all().thenReturn(client_list)

    response = client.get("/client/get-all")
    data = response.json()

    verify(mock_client_repository, atleast=1).get_all()
    assert response.status_code == 200
    assert len(data) == len(client_list)
    for item in data:
        _id = item['client_id']
        assert all((item['document'] == f'document{_id}',
                    item['sur_name'] == f'sur_name_{_id}',
                    item['first_name'] == f'first_name_{_id}',
                    item['patronymic'] == f'patronymic_{_id}',
                    item['birthday'] == date.today().isoformat()))


def test_get_valid_client(client, mock_client_repository, client_list):
    when(mock_client_repository).get_by_id(...).thenReturn(client_list[0])
    _id = 1

    response = client.get(f"/client/get/{_id}")
    data = response.json()

    verify(mock_client_repository, atleast=1).get_by_id(_id)

    assert response.status_code == 200
    assert all((data['document'] == f'document{_id}',
                data['sur_name'] == f'sur_name_{_id}',
                data['first_name'] == f'first_name_{_id}',
                data['patronymic'] == f'patronymic_{_id}',
                data['birthday'] == date.today().isoformat()))


def test_get_invalid_client(client, mock_client_repository, client_list):
    _id = 1
    when(mock_client_repository).get_by_id(...).thenReturn(None)

    response = client.get(f"/client/get/{_id}")
    data = response.json()

    verify(mock_client_repository, atleast=1).get_by_id(_id)

    assert response.status_code == 404
    assert data == {'detail': f'Client with ID {_id} does not exist'}


def test_create_client(client, mock_client_repository, client_list):
    _id = 1
    when(mock_client_repository).create(...).thenReturn(_id)
    when(mock_client_repository).get_by_id(_id).thenReturn(client_list[0])

    response = client.post("/client/create",
                           json={"document": "string",
                                 "sur_name": "string",
                                 "first_name": "string",
                                 "patronymic": "string",
                                 "birthday": date.today().isoformat()})
    data = response.json()

    verify(mock_client_repository, atleast=1).create(...)

    assert response.status_code == 200
    assert all((data['document'] == f'document{_id}',
                data['sur_name'] == f'sur_name_{_id}',
                data['first_name'] == f'first_name_{_id}',
                data['patronymic'] == f'patronymic_{_id}',
                data['birthday'] == date.today().isoformat()))


def test_delete_client(client, mock_client_repository, client_list):
    _id = 1
    when(mock_client_repository).delete(...).thenReturn(True)

    response = client.delete(f"/client/delete/{_id}")

    verify(mock_client_repository, atleast=1).delete(_id)
    assert response.status_code == 200


def test_update_client(client, mock_client_repository, client_list):
    _id = 1
    when(mock_client_repository).get_by_id(_id).thenReturn(client_list[0])
    when(mock_client_repository).update(...).thenReturn(True)

    new_document = "new_document"
    response = client.put("/client/update", json={"client_id": _id, "document": new_document})
    data = response.json()

    # verify(mock_client_repository, atleast=1).update(...)
    assert response.status_code == 200
    assert all((data['document'] == new_document,
                data['sur_name'] == f'sur_name_{_id}',
                data['first_name'] == f'first_name_{_id}',
                data['patronymic'] == f'patronymic_{_id}',
                data['birthday'] == date.today().isoformat()))
