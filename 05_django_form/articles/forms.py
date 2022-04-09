from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder' : 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content form-control',

            }
        ),
        error_messages={
            'required': 'Please enter your content!',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        #exclude = ('title', )제외하고 다 출력
        


# class ArticleForm(forms.Form):
#     # regionA = 'sl'
#     # regionB = 'dj'
#     # regionC = 'bu'
#     # regions_choice = [
#     #     (regionA, '서울'),
#     #     (regionB, '대전'),
#     #     (regionC, '부산'),
#     # ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     # region = forms.ChoiceField(widget=forms.Select, choices=regions_choice)