v<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## Citus

Postgres-inherited dbt adapter for Citus database. Many parts copied from [dbt-greenplum](https://github.com/markporoshin/dbt-greenplum)

### Materializing a Distributed Table

via [`create_distributed_table`](https://docs.citusdata.com/en/v11.0/develop/api_udf.html#create-distributed-table)

```
{{
  config(materialized='table', distribution_column='name')
}}
```

| arg name | required | default value |
| --- | --- | --- |
| distribution_column | no | None |


### Testing

Citus provides an easy way to spin up a local cluster via docker:

```
git clone https://github.com/citusdata/docker
cd docker
docker compose up --scale worker=1
```

Now, you can run the integration tests in this repo:

```
pytest .\tests\functional\adapter\test_distributed.py
```

### Notes

To understand the inner workings, check out the `citus__create_table_as` macros definite in (adapters.sql)[dbt\include\citus\macros\adapters.sql]

```
{% macro citus__create_table_as(temporary, relation, sql) %}
...
{% endmacro %}
```

## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- If one doesn't exist feel free to request a #db-Citus channel be made in the [#channel-requests](https://getdbt.slack.com/archives/C01D8J8AJDA) on dbt community slack channel.
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://community.getdbt.com/), or open [an issue](https://github.com/dbt-labs/dbt-redshift/issues/new)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).