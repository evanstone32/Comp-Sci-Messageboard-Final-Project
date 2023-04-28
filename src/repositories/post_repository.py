from src.models.models import Post,db

_post_repo = None


class PostRepository:
    
#creates a post in database
    def create_post(self, post_id: int, post: str, forum_id: int, user_id) -> Post:
        post = Post(post_id, post, forum_id, user_id)
        db.session.add(post)
        db.session.commit()

#gets all post at a specific forum_id
    def get_all_posts(self,forum_id):
        return Post.query.get(forum_id)
        