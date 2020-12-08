from django import forms

class PostForm(forms.Form):
  title = forms.CharField(max_length=30, label="タイトル")
  # formsにはTextFieldがない為、widgetでtextareaを使う
  content = forms.CharField(label="内容", widget=forms.Textarea())