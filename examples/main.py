from js_loader import install_js_loader
install_js_loader()
from js import bye

print(dir(bye))
print(bye.hello.js_code)
