"""GET endpoints for retreiving profile details."""

from app.services.profile_service import get_profiles

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

    profiles = get_profiles()  # This function should be defined to fetch the profiles
    return {"profiles": profiles}, 200