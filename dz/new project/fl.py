from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kfkkmdkmvslckqpwl4o697rmdll34cwcfemk'


menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Служба поддержки', 'url': 'contact'},
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Каталог товаров", menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title="О компании", menu=menu)


@app.route('/profile/<int:username>')
def profile(username):
    return f"Пользователь: {username}"


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':

        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
