from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_ac import acpype_params_ac


class TestAcpypeParamsACDocker():
    def setup_class(self):
        fx.test_setup(self,'acpype_params_ac_docker')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_ac_docker(self):
        acpype_params_ac(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_frcmod'])
        assert fx.not_empty(self.paths['output_path_inpcrd'])
        assert fx.not_empty(self.paths['output_path_lib'])
        assert fx.not_empty(self.paths['output_path_prmtop'])
        assert fx.equal(self.paths['output_path_frcmod'], self.paths['ref_output_acpype_path_frcmod'])
        assert fx.equal(self.paths['output_path_inpcrd'], self.paths['ref_output_acpype_path_inpcrd'])
        #assert fx.equal(self.paths['output_path_lib'], self.paths['ref_output_acpype_path_lib'])
        #assert fx.equal(self.paths['output_path_prmtop'], self.paths['ref_output_acpype_path_prmtop'])

import pytest
@pytest.mark.skip(reason="singularity currently not available")
class TestAcpypeParamsACSingularity():
    def setup_class(self):
        fx.test_setup(self,'acpype_params_ac_singularity')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_params_ac_singularity(self):
        acpype_params_ac(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_frcmod'])
        assert fx.not_empty(self.paths['output_path_inpcrd'])
        assert fx.not_empty(self.paths['output_path_lib'])
        assert fx.not_empty(self.paths['output_path_prmtop'])
        assert fx.equal(self.paths['output_path_frcmod'], self.paths['ref_output_acpype_path_frcmod'])
        assert fx.equal(self.paths['output_path_inpcrd'], self.paths['ref_output_acpype_path_inpcrd'])
        #assert fx.equal(self.paths['output_path_lib'], self.paths['ref_output_acpype_path_lib'])
        #assert fx.equal(self.paths['output_path_prmtop'], self.paths['ref_output_acpype_path_prmtop'])
