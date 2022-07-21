#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-citus"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.1.0"
description = """The Citus adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="jgensler8",
    author_email="jgensler8@user.noreply.github.com",
    url="https://github.com/jgensler8/dbt-citus",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=["dbt-core=1.1.1", "dbt-postgres=1.1.1"],
)
