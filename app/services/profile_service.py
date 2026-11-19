"""Service layer for RO-Crate profiles requests."""

from flask import Response, current_app, jsonify

from app.profiles import runner

def get_profiles() -> list[str]:
    """
    Retrieve a list of available RO-Crate validation profiles.

    Returns:
    - A JSON response with the list of profiles and an HTTP status code.
    """

    profiles = runner.get_profiles()
    results = []
    for profile in profiles:
        results.append({
            "Identifier": profile.identifier if profile.identifier is not None else "N/A",
            "Name": "\n".join(map(str, profile.name)) if isinstance(profile.name, list) else str(profile.name or ""),
            "Description": profile.description if profile.description is not None else "N/A",
            "Version": profile.version if profile.version is not None else "N/A",
            "URI": profile.uri if profile.uri is not None else "N/A",
            "Based on": "\n".join([p.identifier for p in profile.inherited_profiles]),
            "Requirements Checks (*)": "Hello"
        })


    # Placeholder implementation; replace with actual logic to retrieve profiles
    return {"profiles": results}
