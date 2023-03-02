from django.db import models
from user . models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class post(models.Model):
    caption = models.CharField( max_length=100)
    user = models.ForeignKey(User,related_name='users',on_delete=models.CASCADE,default=True)
    image = models.FileField(default=True,upload_to='static/',max_length=100)
    is_active = models.IntegerField(default=1)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} - post'
    
    def likes_count(self):
       return self.post_likes.all().count()
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return 'id: {}'.format(self.pk)
    
class Like(models.Model):
    Post = models.ForeignKey(post, related_name="post_likes",on_delete = models.CASCADE)
    likeusers = models.ForeignKey(User,related_name="likes",on_delete = models.CASCADE,default=True)
    
   
    
#     def __str__(self):
#         return f"{self.id}--{self.liked_by}--{self.post}"

class question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    title = models.CharField(max_length=500)
    body1 = models.CharField(max_length=500)
    body2 = models.CharField(max_length=500,default=True)
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} - post'
    
    def get_title(self):
        return self.title
    
class question_like(models.Model):
    Question = models.ForeignKey(question,on_delete=models.CASCADE,related_name='likes')
    likeusers = models.ForeignKey(User,on_delete=models.CASCADE,related_name='li')
    

class save_question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True,related_name='saved_user')
    saved_question = models.ForeignKey(question,on_delete=models.CASCADE,default=True,related_name='savess')
    
class comment(models.Model):
    Post = models.ForeignKey(post,related_name='posts',on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) :
        return '%s - %s' % (self.Post.caption,self.Post.user)

class comment_reply(models.Model):
    Comment = models.ForeignKey(comment,related_name='comms',on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
class answers(models.Model):
    Question = models.ForeignKey(question,on_delete=models.CASCADE,related_name='questionss',default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user1')
    answer = models.CharField(max_length=500)
    like = models.IntegerField(default=0)
    
class answer_like(models.Model):
    Answer = models.ForeignKey(answers,on_delete=models.CASCADE,related_name='answerlike')
    liked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_by')
    