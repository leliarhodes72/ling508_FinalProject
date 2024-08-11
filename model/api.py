from flask import Flask, jsonify, request
from services import TarotService

def create_app():
    app = Flask(__name__)

    # Initialize the TarotService
    tarot_service = TarotService()

    # A simple example of how to do a GET method
    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello World!"

    # Implement a GET method called "/get_card/<card_name>" that returns the details of the requested card
    @app.route("/get_card/<card_name>", methods=["GET"])
    def get_card(card_name):
        card = tarot_service.get_tarot_card_by_name(card_name)  # Ensure the service method is called correctly
        if card:
            return jsonify(card)
        else:
            return jsonify({"error": "Card not found"}), 404

    return app

if __name__ == "__main__":
    myapp = create_app()
    myapp.run()