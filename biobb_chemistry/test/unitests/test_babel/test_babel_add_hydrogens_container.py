from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_add_hydrogens import babel_add_hydrogens


class TestBabelAddHydrogensDocker():
    def setUp(self):
        fx.test_setup(self,'babel_add_hydrogens_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_docker(self):
        babel_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])

class TestBabelAddHydrogensSingularity():
    def setUp(self):
        fx.test_setup(self,'babel_add_hydrogens_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_singularity(self):
        babel_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
