"""GET endpoints for retreiving profile details."""

from apiflask import APIBlueprint
from flask import Response

profile_routes_bp = APIBlueprint("profile_routes", "Profiles")


@profile_routes_bp.get("/profiles")
def get_profiles() -> tuple[Response, int]:
    """
    Retrieve a list of available RO-Crate validation profiles.

    Returns:
    - A tuple containing the list of profiles and an HTTP status code.
    """
    # Placeholder implementation; replace with actual logic to retrieve profiles
    profiles = ["profile1", "profile2", "profile3"]
    return {"profiles": profiles}, 200