from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_remove_hydrogens import babel_remove_hydrogens


class TestBabelRemoveHydrogens():
    def setup_class(self):
        fx.test_setup(self, 'babel_remove_hydrogens')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens(self):
        babel_remove_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        # assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
