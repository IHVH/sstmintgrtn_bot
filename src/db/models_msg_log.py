from sqlalchemy import Boolean, Integer, String, Column, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(200), nullable=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    full_name = Column(String(500), nullable=True)
    language_code = Column(String(10), nullable=True)
    is_bot = Column(Boolean, nullable=False, default=False)
    messages = relationship("Message", back_populates="user")

class Chat(Base):
    __tablename__ = 'chats'
    id = Column(BigInteger, primary_key=True)
    bio = Column(String(500), nullable=True)
    description = Column(String(1000), nullable=True)
    messages = relationship("Message", back_populates="chat")

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    user = relationship("User", back_populates="messages")
    chat_id = Column(BigInteger, ForeignKey('chats.id'))
    chat = relationship("Chat", back_populates="messages")
    full_user_name = Column(String(700), nullable=True)
    date_time = Column(DateTime(), default=datetime.now)
    text = Column(String(3000), nullable=True)
    call_data = Column(String(3000), nullable=True)
