# --> Will import all the variables, settings, functions, classes declared or initialized in common.py
from common import *

# Declaring the API Classes required in the project. Same will be linked to API's in main.py.
# Format will be like --> from filename(without the .py extension) import classname
from sign_in import SignInHandler
from sign_up import SignUpHandler
from product import ProductHandler
from product_image import ProductImageHandler
from search_news import SearchNewsHandler
from product_search import ProductSearchHandler
from my_product import MyProductHandler
from single_product import SingleProductHandler
from product_search_history import SearchHistoryHandler


def make_app():
    return tornado.web.Application([
        (r"/julygroup6_web/api/sign_up", SignUpHandler),
        (r"/julygroup6_web/api/sign_in", SignInHandler),
        (r"/julygroup6_web/api/product", ProductHandler),
        (r"/julygroup6_web/api/product/image", ProductImageHandler),
        (r"/julygroup6_web/api/search/news", SearchNewsHandler),
        (r"/julygroup6_web/api/product/search", ProductSearchHandler),
        (r"/julygroup6_web/api/single/product", SingleProductHandler),
        (r"/julygroup6_web/api/product/search/history", SearchHistoryHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8006)
    tornado.ioloop.IOLoop.current().start()
