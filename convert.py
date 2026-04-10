import markdown

with open("convert.py", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)

with open("convert.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(html)