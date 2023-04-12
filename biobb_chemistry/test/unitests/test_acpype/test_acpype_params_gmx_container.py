import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_gmx import acpype_params_gmx


class TestAcpypeParamsGMXDocker():
    def setup_class(self):
        fx.test_setup(self, 'acpype_params_gmx_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_gmx_docker(self):
        acpype_params_gmx(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_gro'])
        assert fx.not_empty(self.paths['output_path_itp'])
        assert fx.not_empty(self.paths['output_path_top'])
        # assert fx.equal(self.paths['output_path_gro'], self.paths['ref_output_acpype_path_gro'])
        # assert fx.equal(self.paths['output_path_itp'], self.paths['ref_output_acpype_path_itp'])
        # assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])


@pytest.mark.skip(reason="singularity currently not available")
class TestAcpypeParamsGMXSingularity():
    def setup_class(self):
        fx.test_setup(self, 'acpype_params_gmx_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_gmx_singularity(self):
        acpype_params_gmx(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_gro'])
        assert fx.not_empty(self.paths['output_path_itp'])
        assert fx.not_empty(self.paths['output_path_top'])
        # assert fx.equal(self.paths['output_path_gro'], self.paths['ref_output_acpype_path_gro'])
        # assert fx.equal(self.paths['output_path_itp'], self.paths['ref_output_acpype_path_itp'])
        # assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])
