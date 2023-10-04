# Імпортуємо необхідні бібліотеки
from flask import Flask, render_template
from datetime import datetime

# Створюємо об'єкт Flask
app = Flask(__name__)

# Встановлюємо маршрут для стартової сторінки ('/')
@app.route('/')
def index():
    # Отримуємо поточну дату та форматуємо її в рядок у форматі 'рік-місяць-день'
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Відображаємо HTML-шаблон 'index.html' і передаємо змінну 'current_date' в шаблон
    return render_template('index.html', current_date=current_date)

# Запускаємо веб-застосунок, якщо цей файл виконується як головний
if __name__ == '__main__':
    app.run(debug=True)