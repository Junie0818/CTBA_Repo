from dash import Dash, html

#Create the Dash app
app = Dash(__name__)
app.title = "My First Dash App"

app.layout = html.Div([
    html.H1("Hello Dash!", style={"color": '#381D5C',
                                  "fontsize": "20px",
                                  "backgroundColor": "#E898AA",}),
    html.P("This is a simple Dash application.", style={"boder": "1px solid black",
                                                        "padding": "100px",
                                                        "margin": "100px"}),
    html.Br(),
    html.A("Click here", href="https://example.com")
                       ])


#Run the app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)