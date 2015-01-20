__all__ = ['base', 'main']

from tornado.web import StaticFileHandler
import os
from app.configparser import config
from .main import (
	MainRoute,
	StaticPageRoute,
	UrlToRedirect,
	FormsHandler,
	CatalogSectionRoute,
	CatalogItemRoute
)

from .testroute import TestRoute

routes = [
	('/', MainRoute),
	('/uploaded-files/(.*)', StaticFileHandler, {"path": os.path.join(os.getcwd(), config('UPLOAD_FILES_PATH'))}),
	('/api/forms/', FormsHandler),

	# TODO :: remove for production (only for development)
	('/test/(.*?).html', TestRoute), ## Only for testing slised pages
	('/test/(.*?)', TestRoute),

	('/([-0-9])+(.html)', UrlToRedirect),
	('/(.*?)/item/(.*?).html', UrlToRedirect),

	('/catalog/(.*?)/(.*?).html', CatalogItemRoute),
	('/catalog/(.*?)/(.*?)', CatalogItemRoute),
	('/catalog/(.*?)', CatalogSectionRoute),
	('/catalog/(.*?).html', CatalogSectionRoute),
	('/(.*?).html', StaticPageRoute),
	('/(.*?)', StaticPageRoute)
]
