from db.repository import Repository
import mysql.connector
import os


class MySQLRepository(Repository):
    def __init__(self):
        config = {
            'user': 'root',  # Update with your MySQL username
            'password': 'root',  # Update with your MySQL password
            'host': 'localhost',  # To run LOCALLY, this should be 'localhost'
            'port': '32000',  # To run LOCALLY, this should be '32000'
            'database': 'tarot'  # Change this to 'tarot' for your project
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def _initialize_database(self):
        init_file_path = os.path.join(os.path.dirname(__file__), 'init.sql')
        with open(init_file_path, 'r') as file:
            sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():  # Execute only non-empty statements
                self.cursor.execute(statement)
        self.connection.commit()
        print("Database initialized successfully.")

    def load_tarot_cards(self) -> list:
        sql = 'SELECT * FROM TarotCards'
        self.cursor.execute(sql)
        entries = [{'id': id, 'name': name, 'description': description}
                   for (id, name, description) in self.cursor]
        return entries

    def get_card(self, card_id: int) -> dict:
        sql = "SELECT * FROM TarotCards WHERE id = %s"
        self.cursor.execute(sql, (card_id,))
        result = self.cursor.fetchone()
        return {'id': result[0], 'name': result[1], 'description': result[2]} if result else None

    def get_all_cards(self) -> list:
        return self.load_tarot_cards()

    def add_card(self, card_data: dict) -> None:
        sql = """
        INSERT INTO TarotCards (name, description, upright_meaning_id, reversed_meaning_id, numerology_id, element_id, astrological_body_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            card_data['name'],
            card_data['description'],
            card_data['upright_meaning_id'],
            card_data['reversed_meaning_id'],
            card_data['keyword'],
            card_data['numerology_id'],
            card_data['element_id'],
            card_data['astrological_body_id']
        )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def get_card_by_name(self, card_name: str) -> dict:
        sql = "SELECT * FROM TarotCards WHERE name = %s"
        self.cursor.execute(sql, (card_name,))
        result = self.cursor.fetchone()
        return {'id': result[0], 'name': result[1], 'description': result[2]} if result else None


# Usage
if __name__ == "__main__":
    mysql_repo = MySQLRepository()
    tarot_cards = mysql_repo.load_tarot_cards()
    print(tarot_cards)  # Print loaded tarot cards