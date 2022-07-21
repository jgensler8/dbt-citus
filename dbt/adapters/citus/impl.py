
from dbt.adapters.sql import SQLAdapter as adapter_cls

from dbt.adapters.postgres.impl import PostgresAdapter
from dbt.adapters.citus import CitusConnectionManager


class CitusAdapter(PostgresAdapter):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """
    ConnectionManager = CitusConnectionManager
