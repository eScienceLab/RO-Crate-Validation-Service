
from app.services.profile_service import get_profiles

from unittest.mock import patch

import pytest
from flask import Flask

@pytest.fixture
def flask_app():
    """Bare app context for functions that only need jsonify."""
    app = Flask(__name__)
    with app.app_context():
        yield app

#@patch("app.services.profile_service.get_profiles")
def test_get_profiles_returns_json_list_of_profiles(mock_list, flask_app):
    response, status = get_profiles()
    assert status == 202
    assert type(response.json.get("profiles", ())) == list
    #mock_list.assert_called_once()