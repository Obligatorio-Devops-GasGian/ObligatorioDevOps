import requests

def test_root_endpoint():
    """Testea que la raíz de vote devuelva 200"""
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
