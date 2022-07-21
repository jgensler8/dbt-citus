/* For examples of how to fill out the macros please refer to the postgres adapter and docs
postgres adapter macros: https://github.com/dbt-labs/dbt-core/blob/main/plugins/postgres/dbt/include/postgres/macros/adapters.sql
dbt docs: https://docs.getdbt.com/docs/contributing/building-a-new-adapter
*/

{% macro citus__create_table_as(temporary, relation, sql) %}
  {%- set distribution_column = config.get('distribution_column', none) -%}
  {{ postgres__create_table_as(temporary, relation, sql) }}
  {% if distribution_column is not none %}
    select create_distributed_table($${{ relation }}$$, '{{ distribution_column }}') ;
  {% endif %}
{% endmacro %}

{% macro citus__alter_column_type(relation,column_name,new_column_type) -%}
'''Changes column name or data type'''
  {{ return(postgres__alter_column_comment(relation, column_dict)) }}
{% endmacro %}

{% macro citus__check_schema_exists(information_schema,schema) -%}
'''Checks if schema name exists and returns number or times it shows up.'''
  {{ return(postgres__check_schema_exists(information_schema, schema)) }}
{% endmacro %}

{% macro citus__create_schema(relation) -%}
'''Creates a new schema in the  target database, if schema already exists, method is a no-op. '''
  {{ return(postgres__create_schema(relation)) }}
{% endmacro %}

{% macro citus__drop_schema(relation) -%}
'''drops a schema in a target database.'''
  {{ return(postgres__drop_schema(relation)) }}
{% endmacro %}

{% macro citus__get_columns_in_relation(relation) -%}
'''Returns a list of Columns in a table.'''
  {{ return(postgres__get_columns_in_relation(relation)) }}
{% endmacro %}

{% macro citus__list_relations_without_caching(schema_relation) -%}
'''creates a table of relations withough using local caching.'''
  {{ return(postgres__list_relations_without_caching(schema_relation)) }}
{% endmacro %}

{% macro citus__list_schemas(database) -%}
'''Returns a table of unique schemas.'''
  {{ return(postgres__list_schemas(database)) }}
{% endmacro %}

{% macro citus__truncate_relation(relation) -%}
'''Removes all rows from a targeted set of tables.'''
  {{ return(postgres__truncate_relation(relation)) }}
{% endmacro %}

{% macro citus__current_timestamp() -%}
'''Returns current UTC time'''
  {{ return(postgres__current_timestamp()) }}
{% endmacro %}
