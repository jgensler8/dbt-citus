import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsCitus(BaseSimpleMaterializations):
    pass


class TestSingularTestsCitus(BaseSingularTests):
    pass


class TestSingularTestsEphemeralCitus(BaseSingularTestsEphemeral):
    pass


class TestEmptyCitus(BaseEmpty):
    pass


class TestEphemeralCitus(BaseEphemeral):
    pass


class TestIncrementalCitus(BaseIncremental):
    pass


class TestGenericTestsCitus(BaseGenericTests):
    pass


class TestSnapshotCheckColsCitus(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampCitus(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethodCitus(BaseAdapterMethod):
    pass
