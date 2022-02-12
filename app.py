import datetime
import streamlit as st
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_date = st.date_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'


pickup_longitude=st.number_input('Pickup longitude')
pickup_latitude=st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count=st.number_input('Passengers count')

#pickup_datetime = datetime.datetime.combine(d, t)


'''

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if st.button('Predict'):
    #pickup_datetime = datetime.datetime.combine(d, t)

    params = {'pickup_datetime':pickup_datetime,
            'pickup_longitude':pickup_longitude,
            'pickup_latitude':pickup_latitude,
            'dropoff_longitude':pickup_longitude,
            'dropoff_latitude':dropoff_latitude,
            'passenger_count':passenger_count}

    prediction=requests.get(url, params=params).json()
    #fare=prediction["fare"]



    st.markdown(str(prediction))
