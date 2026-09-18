from app.core.connections.database import connection


class OrderRepository:
    def __init__(self, connection=connection):
        self.connection = connection()

    def find_order(self, pk_order: int):
        sql = """
            SELECT *
            FROM orders
            WHERE pk_order = %(pk_order)s
        """

        params = {"pk_order": pk_order}

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            data = cursor.fetchone()

        return data
