from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_remove_hydrogens import reduce_remove_hydrogens


class TestReduceRemoveHydrogensDocker():
    def setUp(self):
        fx.test_setup(self,'reduce_remove_hydrogens_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_docker(self):
        reduce_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])

class TestReduceRemoveHydrogensSingularity():
    def setUp(self):
        fx.test_setup(self,'reduce_remove_hydrogens_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_singularity(self):
        reduce_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
