from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_ac import AcpypeParamsAC


class TestAcpypeParamsAC():
    def setUp(self):
        fx.test_setup(self,'acpype_params_ac')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_params_ac(self):
        AcpypeParamsAC(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path_frcmod'])
        assert fx.not_empty(self.paths['output_path_inpcrd'])
        assert fx.not_empty(self.paths['output_path_lib'])
        assert fx.not_empty(self.paths['output_path_prmtop'])
        assert fx.equal(self.paths['output_path_frcmod'], self.paths['ref_output_acpype_path_frcmod'])
        assert fx.equal(self.paths['output_path_inpcrd'], self.paths['ref_output_acpype_path_inpcrd'])
        assert fx.equal(self.paths['output_path_lib'], self.paths['ref_output_acpype_path_lib'])
        assert fx.equal(self.paths['output_path_prmtop'], self.paths['ref_output_acpype_path_prmtop'])
