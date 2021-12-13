import numpy as np

import pandas as pd

fc1 = pd.read_csv('forecast_tbats.csv')
fc2 = pd.read_csv('forecast_holt.csv')

average_fc = pd.read_csv('sample_submission_afcs2021.csv')
print(fc1.iloc[:,1])


for j, column in enumerate(fc1):
	average = []
	if column != "id":
		for i in range(len(fc1[column])):
			
			avg = (fc1[column][i] + fc2[column][i]) /2
			average.append(avg)
		average_fc[column] = average
		if column == "F28":
			print(fc1[column])
			print(average_fc[column])
average_fc.reset_index(drop=True, inplace=True)
average_fc.to_csv('forecast_average.csv',index=False)