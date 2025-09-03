from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input1", type="number", placeholder="Enter a number"),
    dcc.Input(id="input2", type="number", placeholder="Enter another number"),
    dcc.Input(id="input3", type="text", placeholder="Enter some text"),

    html.Div(id="output1"),
    html.Div(id="output2"),
    html.Div(id="output3")

])

@app.callback(
    Output("output1", "children"),
    Output("output2", "children"),
    Output("output3", "children"),

    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value")
)

def update_outputs(num1, num2, text):
    num1 = num1 or 0
    num2 = num2 or 0
    text = text or ""

    result1 = f"The sume of the first 2 numbers is: {num1 + num2}"
    result2 = f"The product of the first 2 numbers is: {num1 * num2}"
    result3 = f"The reversed text of the third cell is: {text}"

    ##add return statement
    return result1, result2, result3


if __name__ == '__main__':
    app.run(debug=True)