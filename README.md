An autonomy validation framework that ingests ROS2 bag data, stores experiment results in PostgreSQL, computes perception, planning, and control KPIs, performs statistical significance testing and confidence interval analysis, applies release-gate safety logic, and visualizes results through an executive validation dashboard

Executive Dashboard: Implement KPI cards, release gauge, radar chart, trend charts, and recent test history.

Domain pages: Add interactive Plotly dashboards for Software Integration, HIL Validation, System Bench Verification, and Vehicle Testing.

Release Gate: Integrate weighted scoring, configurable thresholds, GO/NO-GO logic, and executive recommendations.

Persistence and reporting: Extend the SQLite schema to store all validation domains, support historical trend analysis, and generate exportable release readiness reports.

connect ScenarioEvaluator to test execution results instead of only aggregate metrics, so each scenario can show:

failed test cases
evidence/log links
timestamps
vehicle runs
regression history.