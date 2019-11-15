from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_minimize import BabelMinimize


class TestBabelMinimizeDocker():
    def setUp(self):
        fx.test_setup(self,'babel_minimize_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_minimize_docker(self):
        BabelMinimize(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])

class TestBabelMinimizeSingularity():
    def setUp(self):
        fx.test_setup(self,'babel_minimize_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_minimize_singularity(self):
        BabelMinimize(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
