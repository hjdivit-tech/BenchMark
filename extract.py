import re
import os

html_path = r"c:\Users\hjdiv\Downloads\bench\index.html"
css_path = r"c:\Users\hjdiv\Downloads\bench\style.css"
js_path = r"c:\Users\hjdiv\Downloads\bench\script.js"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract and remove style
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(style_match.group(1).strip() + "\n")
    content = content.replace(style_match.group(0), '<link rel="stylesheet" href="style.css">')
    print("Extracted CSS to style.css")

# Extract and remove script
script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if script_match:
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(script_match.group(1).strip() + "\n")
    content = content.replace(script_match.group(0), '<script src="script.js"></script>')
    print("Extracted JS to script.js")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html")
