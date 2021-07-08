from django import forms


class PlayerStats(forms.Form):
    Player1 = forms.CharField(label="Player 1", max_length=200)
    Season1 = forms.CharField(label="Season", max_length=4)
    Player2 = forms.CharField(label="Player 2", max_length=200)
    Season2 = forms.CharField(label="Season", max_length=4)
