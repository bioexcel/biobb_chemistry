from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_cns import AcpypeParamsCNS


class TestAcpypeParamsCNS():
    def setUp(self):
        fx.test_setup(self,'acpype_params_cns')

    def tearDown(self):
        fx.test_teardown(self)
        pass

    def test_params_cns(self):
        AcpypeParamsCNS(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path_par'])
        assert fx.not_empty(self.paths['output_path_inp'])
        assert fx.not_empty(self.paths['output_path_top'])
        #assert fx.equal(self.paths['output_path_par'], self.paths['ref_output_acpype_path_par'])
        #assert fx.equal(self.paths['output_path_inp'], self.paths['ref_output_acpype_path_inp'])
        #assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])
