import sys, os
import pytest

#sys.path.append(os.path.abspath("../../src/backend"))
from src.backend.crypto import DataCipher



@pytest.fixture
def app():
   app = create_app()
   return app

def test_encrypt():
   cipher = DataCipher()
   encrypted = cipher.encrypt("test")
   assert cipher.decrypt(encrypted) == "test"

