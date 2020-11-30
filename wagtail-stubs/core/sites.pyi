from typing import Any

MATCH_HOSTNAME_PORT: int
MATCH_HOSTNAME_DEFAULT: int
MATCH_DEFAULT: int
MATCH_HOSTNAME: int

def get_site_for_hostname(hostname: Any, port: Any): ...
