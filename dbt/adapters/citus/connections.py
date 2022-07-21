from dataclasses import dataclass
from dbt.adapters.postgres.connections import (
    PostgresCredentials,
    PostgresConnectionManager,
)


@dataclass
class CitusCredentials(PostgresCredentials):
    """
    Defines database specific credentials that get added to
    profiles.yml to connect to new adapter
    """

    @property
    def type(self):
        """Return name of adapter."""
        return "citus"


class CitusConnectionManager(PostgresConnectionManager):
    TYPE = "citus"
