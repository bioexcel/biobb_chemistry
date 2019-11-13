from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_remove_hydrogens import BabelRemoveHydrogens


class TestBabelRemoveHydrogensContainer():
    def setUp(self):
        fx.test_setup(self,'babel_remove_hydrogens_container')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_container(self):
        BabelRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
