'''

This module is to establish a scoring and visualization system for EEG TGAM data for effective learning.
This module takes in EEG TGAM data csv as input, and do a scoring based on the attention and meditation scores to let
the user know how well they are doing in terms of meditation and attention. It will cumulatively score the attention and meditation scores over time, 
and provide a final score at the end of the session.
This not only measures effort in terms of duration but also the quality of time spent in learning process.
Some of the metrics that can be useful for reflection include:
- Average attention score
- Average meditation score
- the total duration of the session
- the final score based on the cumulative attention and meditation scores.
- the standard deviation of the attention and meditation scores.
- the maximum and minimum attention and meditation scores.

It also visualizes the scores using matplotlib.



'''

# first import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read in the csv file
class ScoringAndVisualization:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.attention_scores = self.data['attention'].to_numpy()
        self.meditation_scores = self.data['meditation'].to_numpy()
        self.session_duration = len(self.attention_scores)
        self.average_attention = np.mean(self.attention_scores)
        self.average_meditation = np.mean(self.meditation_scores)
        self.cumulative_attention = np.cumsum(self.attention_scores)
        self.cumulative_meditation = np.cumsum(self.meditation_scores)
        self.attention_deviation = np.std(self.attention_scores)
        self.meditation_deviation = np.std(self.meditation_scores)
        self.effective_learning_time = sum(filter(lambda x: x > 70, self.attention_scores)) #in seconds
        #since the attention score is measured roughly every seconds, labelling time with score >70 to be effective learning time




#testing the class

#initialize the class with a csv file
if __name__ == "__main__":
    csv_file = "path/to/your/csvfile.csv"
    scoring_viz = ScoringAndVisualization(csv_file)

print(scoring_viz.attention_scores)