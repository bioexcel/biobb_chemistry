# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_remove_hydrogens import babel_remove_hydrogens
import sys


class TestBabelRemoveHydrogensDocker():
    def setup_class(self):
        fx.test_setup(self, 'babel_remove_hydrogens_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_docker(self):
        babel_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        # assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestBabelRemoveHydrogensSingularity():
    def setup_class(self):
        fx.test_setup(self, 'babel_remove_hydrogens_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_singularity(self):
        babel_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        # assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
