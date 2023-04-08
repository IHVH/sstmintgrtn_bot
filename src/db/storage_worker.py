from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from typing import List
from db.models_msg_log import Base, User, Chat, Message

class StorageWorker:

    def __init__(self, connection_string: str):
        self.__connection_string = connection_string
        self.__engine = create_engine(self.__connection_string)
        if not database_exists(self.__engine.url):
            create_database(self.__engine.url)
        Base.metadata.create_all(self.__engine)
        self.__db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.__engine))

    def save_message(self, msg: Message):
        with self.__db_session() as db:
            db.add(msg)
            db.commit()

    def save_user(self, user: User)-> User:
        with self.__db_session() as db:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
    
    def save_chat(self, chat: Chat)-> Chat:
        with self.__db_session() as db:
            db.add(chat)
            db.commit()
            db.refresh(chat)
            return chat

    def get_messages(self) -> List[Message]:
        with self.__db_session() as db:
            messages = db.query(Message).all()
            return messages

    def get_user_messages(self, user: User) -> List[Message]:
        with self.__db_session() as db:
            messages = db.query(Message).filter(User.id == user.id).all()
            return messages

    def get_user(self, user_id: str) -> User:
        with self.__db_session() as db:
            user = db.get(User, user_id)
            return user

    def get_chat(self, chat_id: str) -> Chat:
        with self.__db_session() as db:
            chat = db.get(Chat, chat_id)
            return chat
