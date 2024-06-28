from jinja2 import Template


html = """
{%- macro input_field(name, placeholder, type="text") -%}
<p><input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}"></p>
{% endmacro %}

{{ input_field('firstname', 'Имя', 'text') }} 
{{ input_field('lastname', 'Фамилия', 'text') }} 
{{ input_field('address', 'Адрес', 'text') }} 
{{ input_field('phone', 'Телефон', 'tel') }} 
{{ input_field('email', 'Почта', 'email') }} 
"""

tm= Template(html)
msg = tm.render()

print(msg)