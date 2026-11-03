# type: ignore
from importlib.metadata import version
from biobb_common.tools import test_fixtures as fx
from biobb_chemistry.acpype.acpype_convert_amber_to_gmx import acpype_convert_amber_to_gmx


class TestAcpypeAmber2GMX():
    def setup_class(self):
        fx.test_setup(self, 'acpype_convert_amber_to_gmx')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_amber2gmx(self):
        acpype_convert_amber_to_gmx(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_path_gro'])
        assert fx.not_empty(self.paths['output_path_top'])
        assert fx.equal(self.paths['output_path_gro'], self.paths['ref_output_acpype_path_gro'])
        # acpype < 2026.9.2 (only option for Python < 3.12) writes zero masses in [ atomtypes ]
        if tuple(int(n) for n in version('acpype').split('.')[:3]) >= (2026, 9, 2):
            ref_top = self.paths['ref_output_acpype_path_top']
        else:
            ref_top = self.paths['ref_output_acpype_path_top_massless']
        assert fx.equal(self.paths['output_path_top'], ref_top)
