"""Runs rocrate_validator and adapts its output.

This is the boundary to the external profiles fetcher.
"""

import logging
from typing import Optional

from rocrate_validator import services


logger = logging.getLogger(__name__)

def get_profiles() -> list[str]:
    """
    Retrieve a list of available RO-Crate validation profiles using rocrate-validator.

    Returns:
    - A list of profiles available.
    """
    
    return services.get_profiles()