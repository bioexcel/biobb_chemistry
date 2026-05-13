# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_remove_hydrogens import reduce_remove_hydrogens
import sys


class TestReduceRemoveHydrogensDocker():
    def setup_class(self):
        fx.test_setup(self, 'reduce_remove_hydrogens_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_docker(self):
        reduce_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestReduceRemoveHydrogensSingularity():
    def setup_class(self):
        fx.test_setup(self, 'reduce_remove_hydrogens_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_singularity(self):
        reduce_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
