from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens


class TestReduceAddHydrogens():
    def setup_class(self):
        fx.test_setup(self,'reduce_add_hydrogens')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens(self):
        reduce_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_reduce_path'])
