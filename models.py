from sqlalchemy import Column, Integer, String, Text
from dbdb import Base

class User(Base):
	__tablename__ = 'tb_member'
	m_idx = Column(Integer, primary_key=True)
	m_id = Column(String(12), unique=True)
	m_password = Column(String(50), unique=True)

	def __init__(self, m_id=None, m_password=None):
		self.m_id = m_id
		self.m_password = m_password

	def __repr__(self):
		return '<User %r>' % (self.m_id)

class Article(Base):
	__tablename__ = 'tb_board'
	b_idx = Column(Integer, primary_key=True)
	b_title = Column(String(255))
	b_body = Column(Text)
	m_id = Column(String(12))

	def __init__(self, b_title=None, b_body=None, m_id=None):
		self.b_title = b_title
		self.b_body = b_body
		self.m_id = m_id
	
	def __repr__(self):
		return '<Article %r>' % (self.b_title)