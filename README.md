# Steam-reviews-analysis-automatic-pipeline
# Automatic pipeline Steam review analysis pipeline system.

The project automatically: 
1. Downloads reviews from Steam using Steam Reviews API
2. Cleans and preprocess text data
3. Creates new features
4. Applies a trained ML model
5. Generates .txt analytics report

Technologies:
Python, Pandas, Scikit-learn, NumPy, Joblib

Machine Learning pipeline:
1. Parsing data from Steam API with user's given URL
2. Cleaning data
3. Creating features
4. TF-IDF vectorization
5. Logistic Regression
6. Prediction
7. Report generation

Example usage:
I used Battlefield 6 for an example.
Input:
Run analyze_game.py and paste the link you need,
https://store.steampowered.com/app/2807960/Battlefield_6/
Output:
AppID: 2807960
Reviews: 2992
Positive: 63.8%
Negative: 36.2%
Average Playtime: 148.21 hours
Average Model Confidence: 0.68

You also may start the project running main.py file.
That will lead you to more detailed analysis, such as:
Classification report, top positive/negative words,
the most crucial positive/negative features,
model's prediction errors.

The project showed a fairly accurate result when compared to 
the actual ratio of positive to negative in Steam.

Future improvements: 
Multilingual training,
Advanced sentiment analysis,
Model retraining pipeline,
Searching for better model using GridSearchCV.

# Author Erick
Data analysis and machine learning portfolio project
Focus areas: 
-Data analysis
-Python automation pipeline
-Machine learning
-NLP
