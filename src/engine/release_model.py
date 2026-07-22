from dataclasses import dataclass, field
from typing import List, Dict


# ------------------------------------------------------------------
# Perception
# ------------------------------------------------------------------

@dataclass
class PerceptionMetricsModel:
    precision: float
    recall: float
    f1: float
    miss_rate: float


# ------------------------------------------------------------------
# Planning
# ------------------------------------------------------------------

@dataclass
class PlanningMetricsModel:
    lane_error: float
    min_ttc: float
    collision_count: int


# ------------------------------------------------------------------
# Control
# ------------------------------------------------------------------

@dataclass
class ControlMetricsModel:
    tracking_error: float
    avg_acceleration: float
    avg_jerk: float


# ------------------------------------------------------------------
# Software Integration
# ------------------------------------------------------------------

@dataclass
class SoftwareIntegrationModel:
    build_success: float = 0.0
    unit_test_pass: float = 0.0
    integration_test_pass: float = 0.0
    code_coverage: float = 0.0
    misra_compliance: float = 0.0
    static_analysis: float = 0.0


# ------------------------------------------------------------------
# HIL
# ------------------------------------------------------------------

@dataclass
class HILValidationModel:
    signal_quality: float = 0.0
    cpu_load: float = 0.0
    memory_load: float = 0.0
    latency_ms: float = 0.0
    regression_pass: float = 0.0
    watchdog_resets: int = 0


# ------------------------------------------------------------------
# Bench Verification
# ------------------------------------------------------------------

@dataclass
class BenchValidationModel:
    localization: float = 0.0
    perception: float = 0.0
    planning: float = 0.0
    control: float = 0.0
    sensor_fusion: float = 0.0
    scenario_pass: float = 0.0


# ------------------------------------------------------------------
# Vehicle Validation
# ------------------------------------------------------------------

@dataclass
class VehicleValidationModel:
    total_miles: float = 0.0
    urban_miles: float = 0.0
    highway_miles: float = 0.0
    night_miles: float = 0.0
    rain_miles: float = 0.0
    disengagements: int = 0
    interventions: int = 0


# ------------------------------------------------------------------
# Statistics
# ------------------------------------------------------------------

@dataclass
class StatisticsModel:
    pass_rate: float
    pass_rate_ci: Dict
    ttc_ci: Dict
    top_failures: List
    risk_table: List
    recommendation: str


# ------------------------------------------------------------------
# Release Decision
# ------------------------------------------------------------------

@dataclass
class ReleaseDecisionModel:
    score: float
    decision: str


# ------------------------------------------------------------------
# Root Object
# ------------------------------------------------------------------

@dataclass
class ReleaseReadinessModel:

    perception: PerceptionMetricsModel
    planning: PlanningMetricsModel
    control: ControlMetricsModel

    software: SoftwareIntegrationModel
    hil: HILValidationModel
    bench: BenchValidationModel
    vehicle: VehicleValidationModel

    scenarios: List[Dict] = field(default_factory=list)

    statistics: StatisticsModel = None

    release: ReleaseDecisionModel = None
    #release: ReleaseMetrics