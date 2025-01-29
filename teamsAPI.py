from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')
def home():
    return "Traun Tomar"

@app.route('/api/teams')
def teamsapi():

    teams = ipl.teamAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def team_vs_team_api():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    result = ipl.team_vs_team_API(team1,team2)

    return jsonify(result)

app.run(debug=True)

