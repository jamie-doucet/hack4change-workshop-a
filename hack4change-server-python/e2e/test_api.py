import pytest
import requests
 
BASE_URL = "http://localhost:8081"
 
def test_get_endpoint():
       response = requests.get(f"{BASE_URL}/home")
       assert response.status_code == 200
       assert response.text == "Welcome to the Hack4Change Web Server."
 
