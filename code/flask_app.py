from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
#def w209():
#    file="about9.jpg"
#    return render_template("w209.html",file=file)

def disasters_bar():
    return render_template('disasters_bar.html')

@app.route("/disasters_map")
def disasters_map():
    return render_template('disasters_map.html')

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
