from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_remove_hydrogens import BabelRemoveHydrogens


class TestBabelRemoveHydrogensDocker():
    def setUp(self):
        fx.test_setup(self,'babel_remove_hydrogens_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_docker(self):
        BabelRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])

class TestBabelRemoveHydrogensSingularity():
    def setUp(self):
        fx.test_setup(self,'babel_remove_hydrogens_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_remove_hydrogens_singularity(self):
        BabelRemoveHydrogens(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
