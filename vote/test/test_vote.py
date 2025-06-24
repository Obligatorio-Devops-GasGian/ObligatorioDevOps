import requests

def test_root_endpoint():
    """Testea que la raíz de vote devuelva 200"""
    response = requests.get("http://vote:80/")
    assert response.status_code == 200
