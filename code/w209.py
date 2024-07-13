from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/disasters_bar")
def disasters_bar():
    return render_template('disasters_bar.html')

@app.route("/disasters_map")
def disasters_map():
    return render_template('disasters_map.html')

@app.route("/disasters_map_facet")
def disasters_map_facet():
    return render_template('disasters_map_facet.html')

@app.route("/time_line")
def time_line():
    return render_template('time_line.html')

@app.route("/time_anim")
def time_anim():
    return render_template('time_anim.html')

@app.route("/cost_bar")
def cost_bar():
    return render_template('cost_bar.html')


if __name__ == "__main__":
    app.run()
