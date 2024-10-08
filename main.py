from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from general_function import fetch_cards


def get_template_file():
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(
            ["html", "xml"],
        ),
    )

    template = env.get_template("template.html")

    return template


def main():
    cards = fetch_cards()
    template = get_template_file()
    rendered_page = template.render(
        cards=cards,
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(
        ("0.0.0.0", 8000),
        SimpleHTTPRequestHandler,
    )
    server.serve_forever()


if __name__ == "__main__":
    main()
