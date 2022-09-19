from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.babelm.babel_add_hydrogens import babel_add_hydrogens


class TestBabelAddHydrogensDocker():
    def setup_class(self):
        fx.test_setup(self,'babel_add_hydrogens_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_docker(self):
        babel_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestBabelAddHydrogensSingularity():
    def setup_class(self):
        fx.test_setup(self,'babel_add_hydrogens_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_add_hydrogens_singularity(self):
        babel_add_hydrogens(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path'])
        #assert fx.equal(self.paths['output_path'], self.paths['ref_output_babel_path'])
