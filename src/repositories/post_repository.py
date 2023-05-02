from src.models.models import Post,db


class PostRepository:
    
#creates a post in database
    def create_new_post(self, post_id:int, post: str, forum_id: int, user_id: int) -> Post:
        post = Post(post_id=post_id, post=post, forum_id=forum_id, user_id=user_id)
        db.session.add(post)
        db.session.commit()

#gets all post at a specific forum_id
    def get_all_posts(self,forum_id):
        return Post.query.get(forum_id)
    
    def get_num_of_posts(self, f_id):
        return len(Post.query.all())+1
    
_post_repo = PostRepository()
        