from django.test import TestCase
from .models import Comment,Mastery

class CommentModelTests(TestCase):
    def test(self):
        mastery = Mastery(id = 1,mastery_name = "X", mastery_description = "Y")
        comment = Comment(comment_votes = 10, fk_mastery = mastery)
        self.assertIs(comment.commentIsVerified(),False)




        

