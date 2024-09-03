 
from django import forms
from django.core.validators import MaxValueValidator

# Define choices for the dropdowns
TEAMS = [
    ('Sunrisers Hyderabad', 'Sunrisers Hyderabad'),
    ('Mumbai Indians', 'Mumbai Indians'),
    ('Royal Challengers Bangalore', 'Royal Challengers Bangalore'),
    ('Delhi Capitals', 'Delhi Capitals'),
    ('Rajasthan Royals', 'Rajasthan Royals'),
    ('Kolkata Knight Riders', 'Kolkata Knight Riders'),
    ('Kings XI Punjab', 'Kings XI Punjab'),
    ('Chennai Super Kings', 'Chennai Super Kings'),
]

CITIES = [
    ('Hyderabad', 'Hyderabad'),
    ('Indore', 'Indore'),
    ('Bangalore', 'Bangalore'),
    ('Mumbai', 'Mumbai'),
    ('Kolkata', 'Kolkata'),
    ('Delhi', 'Delhi'),
    ('Kanpur', 'Kanpur'),
    ('Jaipur', 'Jaipur'),
    ('Chennai', 'Chennai'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Dharamsala', 'Dharamsala'),
    ('Ranchi', 'Ranchi'),
    ('Abu Dhabi', 'Abu Dhabi'),
    ('Sharjah', 'Sharjah'),
    ('Mohali', 'Mohali'),
]

class PredictionForm(forms.Form):
    batting_team = forms.ChoiceField(choices=TEAMS)
    bowling_team = forms.ChoiceField(choices=TEAMS)
    city = forms.ChoiceField(choices=CITIES)
    total_runs_x = forms.IntegerField(label='Target Runs')
    runs = forms.IntegerField(label='Current Runs')
    overs = forms.FloatField(label='Overs Completed', validators=[MaxValueValidator(19)])
    wickets = forms.IntegerField(label='Wickets Lost', validators=[MaxValueValidator(10)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-0'})

 
