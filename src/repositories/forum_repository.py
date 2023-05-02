from src.models.models import Forum, db


class ForumRepository:


    def create_forum(self, forum_id: int, title: str) -> Forum:
        forum = Forum(forum_id=forum_id, title=title)
        db.session.add(forum)
        db.session.commit()
        return forum

    def get_new_forum_num(self):
        return len(Forum.query.all())+1

    def get_all_forums(self):
        return Forum.query.all()
    
    def get_forum(self, forum_id):
        return Forum.query.get(forum_id)


_forum_repo = ForumRepository()