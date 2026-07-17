CREATE TABLE test_run (
    run_id SERIAL PRIMARY KEY,
    software_version VARCHAR(50),
    scenario_name VARCHAR(100),
    weather VARCHAR(50),
    execution_date TIMESTAMP
);

CREATE TABLE perception_metrics (
    metric_id SERIAL PRIMARY KEY,
    run_id INTEGER REFERENCES test_run(run_id),

    precision FLOAT,
    recall FLOAT,
    f1_score FLOAT,

    missed_pedestrian_rate FLOAT
);

CREATE TABLE planning_metrics (
    metric_id SERIAL PRIMARY KEY,
    run_id INTEGER REFERENCES test_run(run_id),

    lane_error FLOAT,
    min_ttc FLOAT,
    collision_count INTEGER
);

CREATE TABLE control_metrics (
    metric_id SERIAL PRIMARY KEY,
    run_id INTEGER REFERENCES test_run(run_id),

    path_tracking_error FLOAT,
    avg_acceleration FLOAT,
    avg_jerk FLOAT
);

CREATE TABLE risk_events (
    event_id SERIAL PRIMARY KEY,
    run_id INTEGER REFERENCES test_run(run_id),

    severity VARCHAR(20),
    timestamp_sec FLOAT,
    description TEXT
);

CREATE TABLE release_decision (
    release_id SERIAL PRIMARY KEY,
    run_id INTEGER REFERENCES test_run(run_id),

    safety_score FLOAT,
    risk_score FLOAT,
    decision VARCHAR(20)
);