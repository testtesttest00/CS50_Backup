import sqlite3
import json
import random
from flask import Flask, redirect, render_template, request, session, jsonify # wanted to use session["turns"] but ig not needed? lol

TILE = "16"

app = Flask(__name__)


@app.route("/")
def index():
    board = [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15",TILE]]
    return render_template("homepage.html", board=board, turn=0)


@app.route("/update", methods=["POST"])
def move():
    #direction = request.get_data.decode("utf-8")
    #direction = request.get_data(as_text=True) (alternative)
    req = request.get_json()
    turns = req["turns"]
    turn = turns.removeprefix("Turn ").strip()
    turn = int(turn)
    direction = req["dir"]
    board = req["board"]
    board = board.replace("'", '"')
    board_list = json.loads(board)
    def checkwin(board):
        if board == [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15",TILE]]:
            return True
        return False
    def nextmove(board, direction, scramble=False):
        if checkwin(board) and not scramble:
            return False
        x = 0
        y = 0
        flag = False
        for row in board_list:
            y = 0
            for value in row:
                if value == TILE:
                    flag = True
                    break
                y += 1
            if flag:
                break
            x += 1
        directions = {
            "up":(-1,0),
            "down":(1,0),
            "left":(0,-1),
            "right":(0,1)
        }
        new_x = x + directions[direction][0]
        new_y = y + directions[direction][1]
        if new_x not in range(4) or new_y not in range(4):
            return False
        board[x][y] = board[new_x][new_y]
        board[new_x][new_y] = TILE
        return True
    if direction == "scramble":
        if turn == 0:
            for _ in range(random.randint(0,500)):
                nextmove(board_list, random.choice(["up","down","left","right"]), scramble=True)
            turn = 0
        return render_template("board.html", board=board_list, turn=turn)
    if not nextmove(board_list, direction):
        if checkwin(board_list) and turn > 0:
            return render_template("board.html", board=board_list, turn=turn, win="true")
        return render_template("board.html", board=board_list, turn=turn)
    turn += 1
    if checkwin(board_list):
        return render_template("board.html", board=board_list, turn=turn, win="true")
    return render_template("board.html", board=board_list, turn=turn)


@app.route("/leaderboard", methods=["POST"])
def leaderboard():
    req = request.get_json()
    db_con = sqlite3.connect("database.db")

    if req["moves"] != "0":
        name = req["player"]
        moves = int(req["moves"].lstrip("Turn "))

        db = db_con.cursor()
        db.execute("INSERT INTO leaderboard (name, moves) VALUES (?, ?)", (name, moves))
        db_con.commit()

    db = db_con.cursor()
    ranks = db.execute("SELECT name, MIN(moves) as moves FROM leaderboard GROUP BY name ORDER BY moves ASC LIMIT 10")

    #return render_template("leaderboard.html", ranks=ranks.fetchall())
    return jsonify(ranks.fetchall())


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        try:
            c = int(request.form.get("cver"))
            p = int(request.form.get("pver"))
            h = int(request.form.get("hver"))
            long = request.form.get("long")
            for x in [c,p,h]:
                if x not in range(11):
                    raise Exception
        except:
            return render_template("failed.html")

        db_con = sqlite3.connect("database.db")
        db = db_con.cursor()
        db.execute("INSERT INTO survey (c, p, h, long) VALUES (?, ?, ?, ?)", (c, p, h, long))
        db_con.commit()

        return redirect("/")

    else:
        return render_template("survey.html")
