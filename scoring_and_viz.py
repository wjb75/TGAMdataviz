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

It also visualizes the scores using matplotlib with a user defined threshold.



'''

# first import the necessary packages
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection   
import numpy as np
import os
import pandas as pd

#read in the csv file
class ScoringAndVisualization:
    def __init__(self, csv_file, threshold_for_eff_learning = 70):
        self.data = pd.read_csv(csv_file)
        self.threshold_for_eff_learning = threshold_for_eff_learning 
        self.attention_scores = self.data['attention'].to_numpy()
        self.meditation_scores = self.data['meditation'].to_numpy()
        self.session_duration = len(self.attention_scores)
        self.average_attention = np.mean(self.attention_scores)
        self.average_meditation = np.mean(self.meditation_scores)
        self.cumulative_attention = np.cumsum(self.attention_scores)
        self.cumulative_meditation = np.cumsum(self.meditation_scores)
        self.attention_deviation = np.std(self.attention_scores)
        self.meditation_deviation = np.std(self.meditation_scores)
        self.effective_learning_time = sum(map(lambda x: x > self.threshold_for_eff_learning, self.attention_scores)) #in seconds
        #since the attention score is measured roughly every seconds, labelling time with score >70 to be effective learning time
           


    def visualize(self):
        #create a roughly time array
        time = np.arange(self.session_duration)

        # create segments for attention line
        attention_points = np.array([time, self.attention_scores]).T.reshape(-1, 1, 2)
        attention_segments = np.concatenate([attention_points[:-1], attention_points[1:]], axis = 1)

        attention_colors = ['green' if score > self.threshold_for_eff_learning else 'blue' for score in self.attention_scores[:-1]]

        meditation_points = np.array([time, self.meditation_scores]).T.reshape(-1, 1, 2)
        meditation_segments = np.concatenate([meditation_points[:-1], meditation_points[1:]], axis=1)  

        fig, ax  = plt.subplots()
        
        # plot attention line with conditional colors
        attention_lc = LineCollection(attention_segments, colors = attention_colors, linewidths = 2, label = 'Attention')
        ax.add_collection(attention_lc)

        # Plot meditation line in blue
        ax.plot(time, self.meditation_scores, 'm-', label='Meditation', linewidth=2)

        # Set plot properties
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Score')
        ax.set_title('Attention and Meditation Scores Over Time')
    
        # Set axis limits
        ax.set_xlim(0, len(self.attention_scores))
        ax.set_ylim(min(min(self.attention_scores), min(self.meditation_scores)) - 5,
                    max(max(self.attention_scores), max(self.meditation_scores)) + 5)
        
        # Add legend
        ax.legend()
        
        plt.show()

#testing the class

#initialize the class with a csv file
if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    data_dir = os.environ.get('DATA_PATH')
    csv_file = data_dir
    scoring_viz = ScoringAndVisualization(csv_file, 50)

print("The attention scores:")
print(scoring_viz.attention_scores)
print("The cumulative attention scores:")
print(scoring_viz.cumulative_attention)
print("the effective learning time:")
print(scoring_viz.effective_learning_time)
scoring_viz.visualize() #plot the attention and meditation scores