# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_convert import babel_convert


class TestBabelConvert():
    def setup_class(self):
        fx.test_setup(self, 'babel_convert')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_convert(self):
        babel_convert(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        # assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
