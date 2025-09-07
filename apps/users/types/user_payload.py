from typing import TypedDict, Optional

class UserPayload(TypedDict):
    """TypedDict for user payload data."""
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    street: Optional[str]
    postal_code: Optional[str]
    city: Optional[str]
    xp_total: int
