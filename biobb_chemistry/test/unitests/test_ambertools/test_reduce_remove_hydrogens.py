from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_remove_hydrogens import ReduceRemoveHydrogens


class TestReduceRemoveHydrogens():
    def setUp(self):
        fx.test_setup(self,'reduce_remove_hydrogens')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens(self):
        ReduceRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_reduce_path'])
