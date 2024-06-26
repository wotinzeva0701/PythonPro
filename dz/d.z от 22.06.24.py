from jinja2 import Template

new = [
    {'id': 'index', 'text': 'Главная'},
    {'id': 'news', 'text': 'Новости'},
    {'id': 'about', 'text': 'О компании'},
    {'id': 'shop', 'text': 'Магазин'},
    {'id': 'contacts', 'text': 'Контакты'}
]


link = """<ul>
{%- for c in new %}
{%- if c['id'] == 'index' %}
<li><a href="/{{ c['id'] }}" class="active">{{ c['text'] }}</a></li>
{%- else %}
<li><a href="/{{ c['id'] }}">{{ c['text'] }}</a></li>
{%- endif %}
{%- endfor %}
</ul>"""


tm = Template(link)
msg = tm.render(new=new)

print(msg)