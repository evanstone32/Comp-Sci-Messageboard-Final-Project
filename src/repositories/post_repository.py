from src.models.models import Post,db


class PostRepository:
    
#creates a post in database
    def create_new_post(self, post: str, forum_id: int, user_id: int) -> Post:
        post = Post(post=post, forum_id=forum_id, user_id=user_id)
        db.session.add(post)
        db.session.commit()

#gets all post at a specific forum_id
    def get_all_posts(self,forum_id):
        return Post.query.get(forum_id)
    
_post_repo = PostRepository()
        