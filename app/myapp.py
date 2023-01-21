import io
import numpy as np
from flask import Flask, request, escape, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
@app.route("/")
def execute_plot():
    a_param = int(request.args.get('a'))
    b_param = int(request.args.get('b'))
    c_param = int(request.args.get('c'))
    xmin_param = int(request.args.get('xmin'))
    xmax_param = int(request.args.get('xmax'))
    ymin_param = int(request.args.get('ymin'))
    ymax_param = int(request.args.get('ymax'))
    
    x = np.linspace(xmin_param, xmax_param, 1000)
    y = a_param*x**2 + b_param*x + c_param
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_xlim([xmin_param, xmax_param])
    axis.set_ylim([ymin_param, ymax_param])
    axis.plot(x, y)
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')