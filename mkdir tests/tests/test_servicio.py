import requests

def test_respuesta_no_vacia():
    response = requests.get("http://localhost:8083")
    assert response.text != ""

def test_status_ok():
    response = requests.get("http://localhost:8083")
    assert response.status_code == 200