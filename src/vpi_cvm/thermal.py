from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class GpuSample:
    temperature_c: int
    memory_used_mb: int
    memory_total_mb: int
    power_w: float


class NvidiaSmiProbe:
    """Reads NVIDIA telemetry without linking CUDA into the controller process."""

    def sample(self) -> GpuSample:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=temperature.gpu,memory.used,memory.total,power.draw",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=10,
            check=True,
        )
        first_gpu = result.stdout.strip().splitlines()[0]
        temp, used, total, power = [part.strip() for part in first_gpu.split(",")]
        return GpuSample(
            temperature_c=int(float(temp)),
            memory_used_mb=int(float(used)),
            memory_total_mb=int(float(total)),
            power_w=float(power),
        )


@dataclass
class ThermalGuard:
    max_temp_c: int = 82
    resume_temp_c: int = 75
    poll_seconds: float = 5.0

    def __post_init__(self) -> None:
        if self.resume_temp_c >= self.max_temp_c:
            raise ValueError("resume_temp_c must be lower than max_temp_c")

    def should_pause(self, sample: GpuSample) -> bool:
        return sample.temperature_c >= self.max_temp_c

    def wait_until_safe(self, probe: NvidiaSmiProbe) -> None:
        sample = probe.sample()
        if not self.should_pause(sample):
            return
        while sample.temperature_c > self.resume_temp_c:
            time.sleep(self.poll_seconds)
            sample = probe.sample()
