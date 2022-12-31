from . import app as flask_app


def test_hello():
    with flask_app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Server is running"
