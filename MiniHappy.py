from dash import Dash, html

app = Dash(__name__)
app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P("This dashboard will visualize the World Happiness Score"),
    html.Br(),
    html.A("World Happiness Report", href="https://worldhappiness.report/", target="_blank", style={"color": "#606583", "textDecoration": "underline"}),
])

if __name__ == '__main__':
    app.run(debug=True)