frequency_list = ['30 seconds', '1 minutes','10 minutes']
models_list    = ['ConvNet', 'ResNet', 'Inception', 'TransApp', 'Arsenal']
lengths_list   = ['6 hours', '12 hours', '1 Day']
devices_list   = ['WashingMachine', 'Dishwasher', 'Microwave', 'Kettle']
list_name_ts   = ['UKDALE_House2_2013-05', 'UKDALE_House2_2013-06', 'UKDALE_House2_2013-07', 'UKDALE_House2_2013-08', 'UKDALE_House2_2013-09', 'UKDALE_House2_2013-10']

text_description_dataset  = f"""
UKDALE and REFIT are two well-known Smart Meters datasets.

- UKDALE: The UKDALE dataset [31] contains data from 5 houses in the United Kingdom, and includes appliance-level load curves sampled every 6 seconds, as well as the whole-house aggregate data series sampled at 16kHz. Four houses were recorded for over a year and a half, while the 5th house was recorded for 655 days.

- REFIT Dataset: The REFIT project (Personalised Retrofit Decision Support Tools for UK Homes using Smart Home Technology) ran between 2013 and 2015. During this period, 20 houses in the United Kingdom were recorded after being monitored with smart meters and multiple sensors. 
This dataset provides aggregate and individual appliance load curves at 8-second sampling intervals.
"""

text_description_model  = f"""
- ConvNet

- ResNet

- Inception

- TransApp
"""