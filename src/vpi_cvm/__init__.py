"""VPI-CVM: evidence-driven autonomous project control plane."""

from .kernel import CognitiveKernel
from .models import TaskSpec, TaskStatus

__all__ = ["CognitiveKernel", "TaskSpec", "TaskStatus"]
__version__ = "0.1.0"
