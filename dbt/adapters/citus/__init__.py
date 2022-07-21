from dbt.adapters.citus.connections import CitusConnectionManager  # noqa
from dbt.adapters.citus.connections import CitusCredentials
from dbt.adapters.citus.impl import CitusAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import citus


Plugin = AdapterPlugin(
    adapter=CitusAdapter,
    credentials=CitusCredentials,
    include_path=citus.PACKAGE_PATH,
    # need this!
    dependencies=["postgres"],
)
