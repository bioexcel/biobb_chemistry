from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_add_hydrogens import BabelAddHydrogens


class TestBabelAddHydrogens():
    def setUp(self):
        fx.test_setup(self,'babel_add_hydrogens')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens(self):
        BabelAddHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
