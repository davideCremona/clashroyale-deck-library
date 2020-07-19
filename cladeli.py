from flask import Flask, render_template
from flask_qrcode import QRcode
import clashroyale as clr
import utils
import cards

app = Flask(__name__)
qrcode = QRcode(app)

token_clr = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjZjNjZmNmVhLTVjOGQtNGUxNC1iNmE5LWU5MWQ5YzZiYTE1YyIsImlhdCI6MTU5NTA3NzcwOSwic3ViIjoiZGV2ZWxvcGVyL2FmZDc4NzY0LWExNjUtMTM1Zi04ZTNiLWQwY2RiOTFiYjEzMSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI5My4zNi4xNzQuMTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.DI9pmZzT4qYgR6Or4lFy_x-lUCQasrDT0Tqdi17QASFrc2-gX3glnGBY1CsjCyBsbPDss9RUGNAJ6f5uL87QRA"
client_clr = clr.official_api.Client(token_clr)


@app.route('/')
def index():
    return '<h1>Clash Royale Deck Library</h1>'


@app.route('/update')
def update_all_cards():
    cards = client_clr.get_all_cards()
    utils.update_all_cards(cards)
    return "updated cards"


# ---------------------------------------------------------------------
#                                                                 DECKS
# ---------------------------------------------------------------------
@app.route('/decks')
def show_decks():
    return "unimplemented yet"


@app.route('/deck/create')
def create_deck():
    return "unimplemented yet"


@app.route('/deck/<int:deck_id>')
def show_deck(deck_id):
    deck = cards.get_deck_by_id(deck_id)
    deck_link = "https://link.clashroyale.com/deck/en?deck="
    for card in deck['cards']:
        deck_link += "{};".format(card['id'])
    return render_template("deck.html", deck=deck, deck_link=deck_link)


@app.route('/deck/<int:deck_id>/update')
def update_deck(deck_id):
    return "unimplemented yet"


@app.route('/deck/<int:deck_id>/delete')
def delete_deck(deck_id):
    return "unimplemented yet"


# ---------------------------------------------------------------------
#                                                            CATEGORIES
# ---------------------------------------------------------------------
@app.route('/categories')
def show_categories():
    """ Lists all categories """
    return "unimplemented yet"


@app.route('/category/create')
def create_category(id_category):
    """ Page for creating a category """
    return "unimplemented yet"


@app.route('/category/<int:category_id>')
def show_category(category_id):
    """ Shows decks of the selected category """
    return "unimplemented yet"


@app.route('/category/<int:category_id>/update')
def update_category(id_category):
    """ Page for updating a category """
    return "unimplemented yet"


@app.route('/category/<int:category_id>/delete')
def delete_category(id_category):
    """ Delete selected category """
    return "unimplemented yet"


if __name__ == '__main__':
    app.run(debug=True)
