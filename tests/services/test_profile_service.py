
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

@patch("app.services.profile_service.runner.get_profiles")
def test_get_profiles_calls_runner(mock_list, flask_app):
    mock_list.return_value = ["profile1", "profile2", "profile3"]
    try:
        response = get_profiles()
    except Exception as e:
        print(f"Error occurred: {e}")
    mock_list.assert_called_once()

def test_get_profiles(flask_app):
    response = get_profiles()
    assert isinstance(response, list), f"Expected list, got {type(response)}"
    assert len(response) > 0
    for profile in response:
        assert isinstance(profile.get("Identifier", None), str), f"Profile missing Identifier: {profile}"
        assert isinstance(profile.get("Name", None), str), f"Profile missing Name: {profile}"
        assert isinstance(profile.get("Description", None), str), f"Profile missing Description: {profile}"
        assert isinstance(profile.get("Version", None), str), f"Profile missing Version: {profile}"
        assert isinstance(profile.get("URI", None), str), f"Profile missing URI: {profile}"
        assert isinstance(profile.get("Based on", None), str), f"Profile missing Based on: {profile}"
        assert isinstance(profile.get("Requirements Checks (*)", None), str), f"Profile missing Requirements Checks (*): {profile}"
    