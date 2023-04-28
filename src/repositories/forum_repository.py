from src.models.models import Forum, db


class ForumRepository:


    def create_forum(self, form_id: int, title: str, post_id: int) -> Forum:
        forum = Forum(form_id, title, post_id,)
        db.session.add(forum)
        db.session.commit()

    def get_all_forums(self):
        return Forum.query.all()
    
    def get_forum(self, forum_id):
        return Forum.query.get(forum_id)


_user_repo = ForumRepository()