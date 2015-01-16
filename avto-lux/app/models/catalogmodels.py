from sqlalchemy import (
	Column,
	String,
	Integer,
	Boolean,
	DateTime,
	Text,
	ForeignKey
	)
from app.configparser import config
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.orm import relationship
from .dbconnect import Base, dbprefix
from .pagemodels import PageMixin, IdMixin
from sqlalchemy.dialects.postgresql import JSON


class CatalogSectionModel(Base, PageMixin, IdMixin):
	__tablename__ = dbprefix + 'catalog'

	delegate_seo_meta_title = Column(Boolean)
	delegate_seo_meta_keywords = Column(Boolean)
	delegate_seo_meta_descrtption = Column(Boolean)
	delegate_seo_title = Column(Boolean)

	items = relationship('CatalogItemModel')


class CatalogItemModel(Base, PageMixin, IdMixin):
	__tablename__ = dbprefix + 'catalog_items'

	desctiption_text = Column(Text)
	main_image = Column(String(8192))
	images = Column(JSON)

	section_id = Column(Integer, ForeignKey(dbprefix + 'catalog.id'))
	orders = relationship('OrderModel')




	# Inheritance from catalog

	inherit_seo_meta_title = Column(Boolean)
	inherit_seo_meta_keywords = Column(Boolean)
	inherit_seo_meta_descrtption = Column(Boolean)
	inherit_seo_title = Column(Boolean)
