from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_convert import BabelConvert


class TestBabelConvertDocker():
    def setUp(self):
        fx.test_setup(self,'babel_convert_docker')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_convert_docker(self):
        BabelConvert(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])

class TestBabelConvertSingularity():
    def setUp(self):
        fx.test_setup(self,'babel_convert_singularity')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_convert_singularity(self):
        BabelConvert(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path'])
        assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
