from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens


class TestReduceAddHydrogensDocker():
    def setUp(self):
        fx.test_setup(self,'reduce_add_hydrogens_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_docker(self):
        reduce_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])

class TestReduceAddHydrogensSingularity():
    def setUp(self):
        fx.test_setup(self,'reduce_add_hydrogens_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_singularity(self):
        reduce_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
