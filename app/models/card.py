from app import db

class Card (db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    like_count = db.Column(db.Integer, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=False)