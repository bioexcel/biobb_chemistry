from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_params_gmx_opls import AcpypeParamsGMXOPLS


class TestAcpypeParamsGMXOPLSDocker():
    def setUp(self):
        fx.test_setup(self,'acpype_params_gmx_opls_docker')

    def tearDown(self):
        #fx.test_teardown(self)
        pass

    def test_params_gmx_opls_docker(self):
        AcpypeParamsGMXOPLS(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path_itp'])
        assert fx.not_empty(self.paths['output_path_top'])
        #assert fx.equal(self.paths['output_path_itp'], self.paths['ref_output_acpype_path_itp'])
        #assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])

class TestAcpypeParamsGMXOPLSSingularity():
    def setUp(self):
        fx.test_setup(self,'acpype_params_gmx_opls_singularity')

    def tearDown(self):
        #fx.test_teardown(self)
        pass

    def test_params_gmx_opls_singularity(self):
        AcpypeParamsGMXOPLS(properties=self.properties, **self.paths).launch()
        assert fx.not_empty(self.paths['output_path_itp'])
        assert fx.not_empty(self.paths['output_path_top'])
        #assert fx.equal(self.paths['output_path_itp'], self.paths['ref_output_acpype_path_itp'])
        #assert fx.equal(self.paths['output_path_top'], self.paths['ref_output_acpype_path_top'])
