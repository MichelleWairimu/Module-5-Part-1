#
import jinja2
import markupsafe

print(f"Jinja2 module location: {jinja2.__file__}")
print(f"MarkupSafe module location: {markupsafe.__file__}")

print(f"Jinja2 module attributes: {dir(jinja2)}")

