from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens


class TestReduceAddHydrogensDocker():
    def setup_class(self):
        fx.test_setup(self,'reduce_add_hydrogens_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_docker(self):
        reduce_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestReduceAddHydrogensSingularity():
    def setup_class(self):
        fx.test_setup(self,'reduce_add_hydrogens_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_singularity(self):
        reduce_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
