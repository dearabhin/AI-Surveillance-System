from flask import Flask, render_template
import monitoring

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-monitoring', methods=['GET'])
def start_monitoring():
    monitoring.monitor_beach()
    return "Monitoring Started!"

if __name__ == "__main__":
    app.run(debug=True)
