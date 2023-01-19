def test_default(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Projeto Base",
        "version": "0.1.0",
        "ambiente": "testes",
    }


def test_default_no_exist(client):
    response = client.get("/qualquer_url")
    assert response.status_code == 404
    assert response.headers == {
        "content-length": "22",
        "content-type": "application/json",
    }
    assert response.json() == {"detail": "Not Found"}
