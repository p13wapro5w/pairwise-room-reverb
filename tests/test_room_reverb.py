import pytest
import math
from media import room_reverb as mod

CASES = [
    ("blend", 'm.blend_ir(1, 3, 0.5) == approx(2.0)'),
    ("resample", 'm.resample_ir(441, 44100, 48000) == 480'),
    ("doppler", 'm.doppler_delay(1, 10) == approx(5.0)'),
    ("occlusion", 'm.path_occlusion(True) == 0.0'),
    ("portal", 'm.portal_split(1, 0.5) == approx((0.5, 0.5))'),
    ("downmix", 'm.downmix_center(1, 2, 3) == approx(5.5)'),
    ("short", 'm.short_reverb(1, 0) == approx(0.25)'),
    ("pre", 'm.pre_delay(10, 10) == approx(1.0)'),
    ("fade", 'm.energy_crossfade(1, 1, 0.5) == approx(1.0)'),
    ("id", 'm.room_id(3, 2) == "3:2"'),
    ("early", 'm.early_reflection(10, 10) == approx(1.0)'),
    ("late", 'm.late_decay(0.5, 2) == approx(0.367879, rel=1e-5)'),
    ("length", 'm.ir_length(48000, 48000) == 1.0'),
    ("gain", 'm.occlusion_gain(True, 0.5) == 0.0'),
    ("key", 'm.reverb_key("r1", "L") == "r1:L"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
