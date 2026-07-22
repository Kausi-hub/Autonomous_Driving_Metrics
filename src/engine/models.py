from dataclasses import dataclass
from enum import Enum

# Release Decision

class ReleaseDecision(str, Enum):

    PASS = "PASS"
    CONDITIONAL = "CONDITIONAL"
    FAIL = "FAIL"

# Perception Domain

@dataclass
class PerceptionMetrics:

    precision: float
    recall: float
    f1: float
    miss_rate: float

# Planning Domain

@dataclass
class PlanningMetrics:

    lane_error: float
    min_ttc: float
    comfort_score: float

# Control Domain

@dataclass
class ControlMetrics:

    tracking_error: float
    avg_jerk: float
    stability_score: float

# Software Integration

@dataclass
class SoftwareIntegrationMetrics:

    build_success_rate: float
    unit_test_pass_rate: float
    static_analysis_score: float
    defect_density: float
    integration_status: str

# HIL Validation

@dataclass
class HILValidationMetrics:

    test_cases_total: int
    test_cases_passed: int
    coverage: float
    fault_injection_pass_rate: float
    hil_status: str

# Bench Validation

@dataclass
class BenchValidationMetrics:

    tests_executed: int
    pass_rate: float
    thermal_margin: float
    performance_margin: float
    bench_status: str

# Vehicle Validation

@dataclass
class VehicleValidationMetrics:

    miles_completed: float
    disengagement_rate: float
    safety_events: int
    vehicle_status: str

# Statistics

@dataclass
class StatisticsMetrics:

    pass_rate: float
    recommendation: str

# Release Gate

@dataclass
class ReleaseMetrics:

    score: float
    decision: ReleaseDecision

@dataclass
class ScenarioResult:

    scenario: str
    passed: bool
    failures: list[str]

@dataclass
class FailureMode:

    failure: str
    count: int

@dataclass
class RiskItem:

    scenario: str
    risk: str
    failures: list[str]

@dataclass
class FailureAnalysisResult:

    top_failures: list[FailureMode]
    risk_ranking: list[RiskItem]
    recommendation: str

# Master Model

@dataclass
class ReleaseReadinessModel:

    perception: PerceptionMetrics
    planning: PlanningMetrics
    control: ControlMetrics
    software: SoftwareIntegrationMetrics
    hil: HILValidationMetrics
    bench: BenchValidationMetrics
    vehicle: VehicleValidationMetrics
    statistics: StatisticsMetrics
    release: ReleaseMetrics
    failure_analysis: FailureAnalysisResult