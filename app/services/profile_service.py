"""Service layer for RO-Crate profiles requests."""

from flask import Response, current_app, jsonify

def get_profiles() -> list[str]:
    """
    Retrieve a list of available RO-Crate validation profiles.

    Returns:
    - A JSON response with the list of profiles and an HTTP status code.
    """
    # Placeholder implementation; replace with actual logic to retrieve profiles
    return jsonify({"profiles": ["profile1", "profile2", "profile3"]}), 202
