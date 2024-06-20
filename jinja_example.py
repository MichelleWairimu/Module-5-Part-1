import jinja2

env = jinja2.Environment()
template = env.from_string("""
My favorite books are:
{% for book in books %}
- {{ book }}
{% endfor %}
""")
print(template.render(books=["Lord of Light", "Free Fall"]))