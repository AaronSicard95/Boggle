from boggle import Boggle
from flask import Flask, request, render_template

boggle_game = Boggle()
app = Flask(__name__)
app.run(host='0.0.0.0', port=6767)
highScore = 0


@app.route('/')
def newB():
    boggle_game.board = boggle_game.make_board()
    return render_template('boggleBoard.html', board = boggle_game.board)

@app.route('/checkWord/<word>')
def checkValid(word):
    return boggle_game.check_valid_word(boggle_game.board, word)

@app.route('/dictexists')
def checkDict():
    words = boggle_game.read_dict('words.txt')
    return words[200]

@app.route('/results', methods=["POST"])
def handleResults():
    global highScore
    data = request.json
    if int(data['score'])>highScore:
        highScore = int(data['score'])
    return data.get('score')

    
@app.route('/gethighscore')
def getHS():
    global highScore
    try:
        return str(highScore)
    except:
        return '0'