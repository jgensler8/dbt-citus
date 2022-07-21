import pytest
from dbt.tests.adapter.basic.files import (
    model_base,
    schema_base_yml,
    seeds_base_csv
)
from dbt.tests.util import (
    run_dbt,
)


config_distributed_table = """
{{ config(materialized='table', distribution_column='name') }}
"""
distributed_table_sql = config_distributed_table + model_base


class TestDistributedTable():
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "distributed_table.sql": distributed_table_sql,
            "schema.yml": schema_base_yml,
        }

    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "base.csv": seeds_base_csv,
        }

    @pytest.fixture(scope="class")
    def project_config_update(self):
        return {
            "name": "base",
        }

    def test_base(self, project):
        results = run_dbt(["seed"])
        assert len(results) == 1

        results = run_dbt()
        assert len(results) == 1