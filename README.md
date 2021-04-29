## Using Descriptions to Classify Chardonnays

In this project I will be using various classification models to predict whether a chardonnay is from France or the United States. To do this, we have extracted a subset of data from zackthoutt on kaggle with 150,000 wine reviews scraped from [WineEnthuiast](https://www.wineenthusiast.com). In the CSV file, the most interesting column was a description of wines by reviewers like this review of a Napa Valley Cabernet from the Heitz Cellar:

"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."

---
### First Run
This is a simplified first step toward a total classification or wines based on descriptive characteristics. To this end, we hand selected 50 features (moderately engineered) that we will use to build a binary matrix to train different classification models with. The feature functions can be found in the word_finder_chard.ipynb file. As expected, there are certain words that are excellent predictors of American and French wines. Almost every model tested above expectations on unseen testing data. A full outline of the processes and code for all the models and data manipulation is found in the US_vs_French_Chard.ipynb.  

Using an proprietary stacking model, we took weighted votes from seven models: k-nearest neighbors, naive bayes, logistic regression, support vector machines, decision tree, random forest, and an XGBoost model. Random Forest and a heavily manufactured XGBoost outperformed the pack and were given extra voting power. On unseen wine descriptions, our stacked model correctly identified 92.5% of the holdout data with a precision of 0.841 and a recall of 0.865. 

### Second Run
In the second time around, we took the descriptions and used the power of the TF-IDF Vectorizer to make a more powerful predictor using all the words in the corpus. At this point, we used a random forest classifier to predict the proper classification. A walkthough can be found in TF-IDF_classifcation.ipynb, located in the streamlit_files folder. This model we used to build an app that is interactive for anybody interested in how the model could predict their own descriptions.

To test the model on your own descriptions, please feel free to download the streamlit files for code to get the data formatted, fit the model, and run the streamlit application. If time permits, the application will be published for everyday use.







