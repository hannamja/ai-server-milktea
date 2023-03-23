from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    question = request.form.get('question')
    Pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
                "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    print(question)
    return render_template('result.html', len=len(Pokemons), Pokemons=Pokemons, question = question)


if __name__ == "__main__":
    app.run(debug=True)
