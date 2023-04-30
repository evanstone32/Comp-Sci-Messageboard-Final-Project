from src.models.models import Comment,db


class CommentRepository:
    
#creates a comment in database
    def create_new_comment(self, comment: str, post_id: int, user_id: int) -> Comment:
        comments = Comment(comment=comment, post_id=post_id, user_id=user_id)
        db.session.add(comments)
        db.session.commit()

#gets all comments at a specific forum_id
    def get_all_comment(self,post_id):
        return Comment.query.get(post_id)
    
_comment_repo = CommentRepository()