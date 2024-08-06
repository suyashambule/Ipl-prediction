import pickle
import pandas as pd
import streamlit as st

teams = ['Royal Challengers Bangalore', 'Mumbai Indians', 'Kolkata Knight Riders', 'Rajasthan Royals',
         'Chennai Super Kings', 'Sunrisers Hyderabad', 'Delhi Capitals', 'Punjab Kings',
         'Lucknow Super Giants', 'Gujarat Titans']

cities = ['Bangalore', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai', 'Jaipur', 'Cape Town',
          'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi',  'Bengaluru', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow',
          'Guwahati', 'Chandigarh', 'Dharamsala', 'Mohali']

pipe = pickle.load(open('pipes.pkl', 'rb'))

st.title('IPL Win Prediction')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select city', sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')

with col4:
    overs = st.number_input('Overs completed')

with col5:
    wickets = st.number_input('Wickets gone')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left*6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'current_rate': [crr],
        'required_rate': [rrr]
    })

    result = pipe.predict_proba(input_df)
    win = result[0][0]
    loss=result[0][1]
    st.text(batting_team+'-'+str((win*100))+"%")
    st.text(bowling_team + '-' + str((loss*100)) + "%")

