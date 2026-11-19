"""Tests for the profiles runner that wraps rocrate_validator."""

import json

from app.profiles import runner


def test_get_profiles_no_inputs():
    """Test that get_profiles returns a list of profiles."""
    profiles = runner.get_profiles()
    assert profiles is not None