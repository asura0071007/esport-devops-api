from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Le design de ton interface frontend
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tournoi eSport 2026 | Leaderboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0b0c10; color: #c5c6c7; display: flex; flex-direction: column; align-items: center; padding: 40px 20px; min-height: 100vh; }
        .header { text-align: center; margin-bottom: 40px; }
        .header h1 { color: #66fcf1; font-size: 36px; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px rgba(102, 252, 241, 0.5); }
        .header p { color: #45a29e; font-size: 16px; margin-top: 5px; text-transform: uppercase; letter-spacing: 1px; }
        .board { background-color: #1f2833; border-radius: 12px; width: 100%; max-width: 600px; padding: 25px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5); border: 1px solid #45a29e; }
        .title { color: #ffffff; font-size: 22px; margin-bottom: 25px; text-align: center; border-bottom: 2px solid #45a29e; padding-bottom: 15px; display: flex; justify-content: center; align-items: center; gap: 10px; }
        .player { display: flex; justify-content: space-between; padding: 15px 20px; margin-bottom: 12px; background-color: #0b0c10; border-left: 5px solid #66fcf1; border-radius: 6px; transition: all 0.3s ease; }
        .player:hover { transform: translateX(8px); box-shadow: -5px 5px 15px rgba(0,0,0,0.4); }
        .rank { font-weight: 800; font-size: 18px; width: 40px; }
        .name { flex-grow: 1; color: #ffffff; font-weight: 600; font-size: 18px; letter-spacing: 0.5px; }
        .score { font-weight: bold; font-size: 18px; }
        
        /* Couleurs du podium */
        .rank-1 { border-left-color: #ffd700; }
        .rank-1 .rank, .rank-1 .score { color: #ffd700; }
        .rank-2 { border-left-color: #c0c0c0; }
        .rank-2 .rank, .rank-2 .score { color: #c0c0c0; }
        .rank-3 { border-left-color: #cd7f32; }
        .rank-3 .rank, .rank-3 .score { color: #cd7f32; }
        
        .footer { margin-top: auto; padding-top: 30px; font-size: 12px; color: #45a29e; text-align: center; }
    </style>
</head>
<body>
    <div class="header">
        <h1>DevOps eSport Cup</h1>
        <p>Live Leaderboard - Call of Duty Mobile</p>
    </div>
    <div class="board">
        <div class="title">🏆 Top Classement Général</div>
        <div class="player rank-1">
            <span class="rank">#1</span>
            <span class="name">Pops_Deha</span>
            <span class="score">9850 pts</span>
        </div>
        <div class="player rank-2">
            <span class="rank">#2</span>
            <span class="name">Laye_Sniper</span>
            <span class="score">9200 pts</span>
        </div>
        <div class="player rank-3">
            <span class="rank">#3</span>
            <span class="name">Goudiaby_Pro</span>
            <span class="score">8900 pts</span>
        </div>
    </div>
    <div class="footer">
        Déployé via Docker | Pipeline CI/CD 2026
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/data')
def api_data():
    # Garde quand même les données brutes dispos pour les machines
    return jsonify({"status": "online", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)