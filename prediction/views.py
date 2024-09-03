import pickle
from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd

# Load the model
with open('/Users/Dell/Desktop/ipl_predictor/ipl_predictor/prediction/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_win(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            batting_team = form.cleaned_data['batting_team']
            bowling_team = form.cleaned_data['bowling_team']
            city = form.cleaned_data['city']
            total_runs_x = form.cleaned_data['total_runs_x']
            overs = form.cleaned_data['overs']
            wickets =10 - form.cleaned_data['wickets']
            # Calculate derived features
            ball_left = 120 - (overs * 6)
            runs_left = total_runs_x - form.cleaned_data['runs']
            crr = form.cleaned_data['runs'] / overs
            rr = runs_left / (ball_left / 6)

            # Prepare the input data for the model as a DataFrame
            input_data = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'city': [city],
                'runs_left': [runs_left],
                'ball_left': [ball_left],
                'wickets': [wickets],
                'total_runs_x': [total_runs_x],
                'crr': [crr],
                'rr': [rr]
            })
    
            # Make prediction
            win_probability = model.predict_proba(input_data)[0][1]*100
            losing_probalility=model.predict_proba(input_data)[0][0]*100
            if wickets == 0:
                win_probability=0
                losing_probalility=100
            # print(wickets)  
            print(win_probability)  
            context = {
                'form': form,
                'win_probability': win_probability,
                'losing_probalility':  losing_probalility,
                'batting_team':  batting_team,
                'bowling_team':bowling_team
        }

            return render(request, 'prediction/prediction.html', context)
    else:
        form = PredictionForm()

    return render(request, 'prediction/prediction.html', {'form': form})
