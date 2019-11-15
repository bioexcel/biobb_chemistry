from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_remove_hydrogens import ReduceRemoveHydrogens


class TestReduceRemoveHydrogensDocker():
    def setUp(self):
        fx.test_setup(self,'reduce_remove_hydrogens_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_docker(self):
        ReduceRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])

class TestReduceRemoveHydrogensSingularity():
    def setUp(self):
        fx.test_setup(self,'reduce_remove_hydrogens_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_singularity(self):
        ReduceRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
