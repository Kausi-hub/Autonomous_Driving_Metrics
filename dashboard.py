from dash import Dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)
precision = 0.917
recall = 0.952
lane_error = 0.187
ttc = 0.9
pass_rate = 0.20
release_recommendation = "FAIL"
risk_table = [
    {"scenario": "Emergency Braking", "risk": "HIGH"},
    {"scenario": "Highway Merge", "risk": "MEDIUM"},
    {"scenario": "Lane Change", "risk": "MEDIUM"},
    {"scenario": "Pedestrian Crossing", "risk": "MEDIUM"},
    {"scenario": "Construction Zone", "risk": "LOW"}
]
top_failures = [("Unsafe TTC", 3),("Poor Detection Precision", 1),("Missed Pedestrian", 1)]
pass_rate_ci = {"lower": 0.036,"upper": 0.624}
app.layout = html.Div([
    html.H1("Autonomous Driving Validation Dashboard"),
    html.Div([
        html.H3(f"Precision: {precision:.3f}"),
        html.H3(f"Recall: {recall:.3f}"),
        html.H3(f"Lane Error: {lane_error:.3f}"),
        html.H3(f"Min TTC: {ttc:.2f} sec")
    ])
])
executive_summary = html.Div(
    [
        html.H2("Executive Summary"),
        html.P("Scenario coverage: 5"),
        html.P("Highest risk area: Emergency Braking"),
        html.P("Most common failure mode: Unsafe TTC"),
        html.P(f"Release Recommendation: {release_recommendation}")
    ]
)
radar = go.Figure()
radar.add_trace(
    go.Scatterpolar(
        r=[92,90,85,94],
        theta=["Perception","Planning","Control","Safety"],
        fill='toself'
    )
)
planning_df = pd.read_csv("data/raw/planning.csv")
ttc_chart = px.line(planning_df,x="timestamp",y="ttc",title="Time To Collision Trend")
lane_chart = px.line(planning_df,x="timestamp",y="lane_error",title="Lane Error")
release_card = html.Div(
    [
        html.H2("Release Recommendation"),
        html.H1(
            release_recommendation,
            style={"color": "green" if release_recommendation == "PASS" else "red"}
        )
    ],
    style={"border": "1px solid black","padding": "20px","margin": "10px"}
)
pass_rate_card = html.Div(
    [
        html.H2("Scenario Pass Rate"),
        html.H1(f"{pass_rate * 100:.1f}%")
    ],
    style={"border": "1px solid black", "padding": "20px", "margin": "10px"}
)
confidence_card = html.Div(
    [
        html.H2("95% Confidence Interval"),
        html.P(
            f"{pass_rate_ci['lower']*100:.1f}% "
            f"to "
            f"{pass_rate_ci['upper']*100:.1f}%"
        )
    ],
    style={"border": "1px solid black","padding": "20px","margin": "10px"}
)
top_failure_card = html.Div(
    [
        html.H2("Top Failure Modes"),
        html.Ul([html.Li(f"{failure}: {count}") for failure, count in top_failures])
    ],
    style={"border": "1px solid black","padding": "20px","margin": "10px"}
)
risk_card = html.Div(
    [
        html.H2("Scenario Risk Ranking"),
        html.Ul([html.Li(f"{item['scenario']} " f"({item['risk']})") for item in risk_table])
    ],
    style={"border": "1px solid black","padding": "20px","margin": "10px"}
)
summary_row = html.Div(
    [release_card,pass_rate_card,confidence_card],
    style={"display": "flex","gap": "20px"}
)
scenario_card = html.Div(
    [
        html.H2("Scenario Evaluation"),
        html.Table(
            [html.Tr([html.Th("Scenario"),html.Th("Risk")])] +
            [
                html.Tr([html.Td(item["scenario"]), html.Td(item["risk"])])
                for item
                in risk_table
            ]
        )
    ],
    style={"border": "1px solid black","padding": "20px","margin": "10px"}
)

app.layout = html.Div([

    html.H1("Autonomous Validation Dashboard"),
    executive_summary,
    summary_row,
    scenario_card,
    risk_card,
    top_failure_card,
    dcc.Graph(figure=radar),
    dcc.Graph(figure=ttc_chart),
    dcc.Graph(figure=lane_chart)
])

if __name__ == "__main__":
    app.run(debug=True)
