from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

db = SQLAlchemy()
class TypeMedia (enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)


class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped["User"] = relationship()
    user_to_id: Mapped["User"] = relationship()


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[TypeMedia] = mapped_column(Enum(TypeMedia, name = "typemedia",native_enum=False),nullable=False)
    url: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    post_id: Mapped["Post"] = relationship()

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped["User"] = relationship()
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column( unique=True, nullable=False)
    author_id: Mapped["User"] = relationship()
    post_id: Mapped["User"] = relationship()
    
          


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
