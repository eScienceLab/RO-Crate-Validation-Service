"""GET endpoints for retreiving profile details."""

from apiflask import APIBlueprint

from app.services import profile_service

profile_routes_bp = APIBlueprint("profile_routes", "Profiles")


@profile_routes_bp.get("/profiles")
def get_profiles():
    """
    Retrieve a list of available RO-Crate validation profiles.

    Returns:
    - A tuple containing the list of profiles and an HTTP status code.
    """

    profiles = profile_service.get_profiles()
    return {"profiles": profiles}, 200
