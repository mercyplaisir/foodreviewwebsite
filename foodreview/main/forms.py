from django import forms

STARS = [('1',1),('2',2),('3',3),('4',4),('5',5)]

class CreateNewReviews(forms.Form):
    comment = forms.CharField(label="comment",max_length=2000)
    stars = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STARS,
    )

