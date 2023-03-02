from django.contrib import admin
from django.urls import path
from.views import *


urlpatterns = [
    path('post1',post1,name='post'),
    path('postview',postview,name='view'),
    path('like/<int:id>',LikeView.as_view(),name='like_view'),
    path('questions',questions,name='questions'),
    path('questionview',questionview,name='questionview'),
    path('questiondetail/<int:id>',questiondetail,name='questiondetail'),
    path('add_comment',add_comment,name='add_comment'),
    path('comment_view/<int:id>',comment_view,name='comment_view'),
    path('like_view/<int:id>',like_views,name='like_view'),
    path('question_likes/<int:id>',question_likes.as_view(),name='question_likes'),
    path('answers',answers_to,name='answers'),
    path('answer_view/<int:id>',answer_view,name='answer_view'),
    path('dislike/<int:id>',dislike.as_view(),name='dislike'),
    path('answer_likes/<int:id>',answer_likesss.as_view(),name='question_likes'),
    path('answer_dislike/<int:id>',answer_dislike.as_view(),name='answer_dislike'),
    path('add_reply',add_reply,name='add_reply'),
    path('save_question',saved_question,name='save_question'),
    path('view_saved/<int:id>',view_saved,name='view_saved'),
    path('blockpost/<int:id>',blockpost,name='blockpost'),
    path('admin_post',admin_post,name='admin_post'),
    path('postcount',postcount,name='postcount'),
    path('questioncount',questioncount,name='questioncount'),
    path('popularposts',popularposts,name='popularposts')
    
]