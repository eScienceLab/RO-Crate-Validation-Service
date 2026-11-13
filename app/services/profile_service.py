"""Service layer for RO-Crate profiles requests."""

from flask import Response, current_app, jsonify

from app.profiles.runner import get_profiles

def get_profiles() -> list[str]:
    """
    Retrieve a list of available RO-Crate validation profiles.

    Returns:
    - A JSON response with the list of profiles and an HTTP status code.
    """

    profiles = get_profiles()

    # Placeholder implementation; replace with actual logic to retrieve profiles
    return jsonify({"profiles": profiles}), 202
