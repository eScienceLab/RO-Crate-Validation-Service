"""Runs rocrate_validator and adapts its output.

This is the boundary to the external profiles fetcher.
"""

import logging

from rocrate_validator import services
from rocrate_validator.models import Profile

logger = logging.getLogger(__name__)


def get_profiles() -> list[Profile]:
    """
    Retrieve a list of available RO-Crate validation profiles using rocrate-validator.

    Returns:
    - A list of profiles available.
    """

    return services.get_profiles()
