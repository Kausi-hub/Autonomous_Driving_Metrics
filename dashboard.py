from pathlib import Path

from src.engine.metrics_engine import MetricsEngine


PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

engine = MetricsEngine(
    PROJECT_ROOT / "data" / "raw"
)

model = engine.run()

print("=" * 60)
print("AUTONOMOUS DRIVING RELEASE READINESS")
print("=" * 60)

print(model.release)