from vpi_cvm.thermal import GpuSample, ThermalGuard


def test_thermal_guard_pauses_at_threshold():
    guard = ThermalGuard(max_temp_c=82, resume_temp_c=75)
    hot = GpuSample(
        temperature_c=83,
        memory_used_mb=1000,
        memory_total_mb=12000,
        power_w=150.0,
    )
    cool = GpuSample(
        temperature_c=74,
        memory_used_mb=1000,
        memory_total_mb=12000,
        power_w=150.0,
    )
    assert guard.should_pause(hot)
    assert not guard.should_pause(cool)
