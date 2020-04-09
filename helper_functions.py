import pandas as pd 
import os

def package_submission(predictions):

	result_frame = pd.DataFrame(data = {'Label': predictions})
	result_frame = result_frame.reset_index()
	result_frame['index'] = result_frame['index'] + 1
	result_frame.columns = ['ImageId', 'Label']

	return result_frame

