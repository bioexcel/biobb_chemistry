# type: ignore
import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_cns import acpype_params_cns


class TestAcpypeParamsCNSDocker():
    def setup_class(self):
        fx.test_setup(self, 'acpype_params_cns_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_cns_docker(self):
        acpype_params_cns(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_par'])
        assert fx.not_empty(self.paths['output_path_inp'])
        assert fx.not_empty(self.paths['output_path_top'])
        # assert fx.equal(self.paths['output_path_inp'], self.paths['ref_output_acpype_path_inp'])
        # assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])


@pytest.mark.skip(reason="singularity currently not available")
class TestAcpypeParamsCNSSingularity():
    def setup_class(self):
        fx.test_setup(self, 'acpype_params_cns_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_cns_singularity(self):
        acpype_params_cns(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_par'])
        assert fx.not_empty(self.paths['output_path_inp'])
        assert fx.not_empty(self.paths['output_path_top'])
        # assert fx.equal(self.paths['output_path_inp'], self.paths['ref_output_acpype_path_inp'])
        # assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])
