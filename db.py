import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def answer_question(self, question):
        """Ответ на вопрос"""
        "Добавление % к каждому слову"
        strTemp = question.split(' ')
        question = ""
        for c in strTemp:
            c = "%" + c + "%"
            question += c
        result = self.cursor.execute("SELECT `answer` FROM `questions` WHERE `question` LIKE ?", (question,))
        return result.fetchall()

    def add_user2(self, user_id, selected_student_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`,'selected_student_id') VALUES (?, ?)",
                            (user_id, selected_student_id,))
        return self.conn.commit()

    def find_user(self, name):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT 'id' FROM `students` WHERE `name` = ?", (name,))
        return int(len(result.fetchall()))

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, operation, value):
        """Создаем запись о доходах/расходах"""
        self.cursor.execute("INSERT INTO `records` (`users_id`, `operation`, `value`) VALUES (?, ?, ?)",
            (self.get_user_id(user_id),
            operation == "+",
            value))
        return self.conn.commit()

    def get_records(self, user_id, within = "all"):
        """Получаем историю о доходах/расходах"""

        if(within == "day"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "week"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "month"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        else:
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? ORDER BY `date`",
                (self.get_user_id(user_id),))

        return result.fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()