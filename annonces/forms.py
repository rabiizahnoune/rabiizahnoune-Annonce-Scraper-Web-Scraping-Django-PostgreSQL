from django import forms

class ScrapingForm(forms.Form):

    pages = forms.IntegerField(min_value=1, label='Nombre de pages', initial=1)  # Use IntegerField for page count
    niche_choices = [
        ('a_vendre', 'Appartement à vendre'),
        ('a_louer', 'Appartement à louer'),
        ('studio', 'Studio'),
        ('T1', 'T1'),
        ('T2', 'T2'),
    ]
    niche = forms.ChoiceField(choices=niche_choices, label='Niche des choix')  # Use ChoiceField for choices

