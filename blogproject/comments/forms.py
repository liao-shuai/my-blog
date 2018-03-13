#  _*_ coding:utf-8  _*_

from django import forms

from comments.models import Comment

#  https://www.zmrenwu.com/post/14/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']