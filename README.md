## Using Descriptions to Classify Chardonnays

In this project I will be using various classification models to predict whether a chardonnay is from France or the United States. To do this, we have extracted a subset of data from zackthoutt on kaggle with 150,000 wine reviews scraped from [WineEnthuiast](https://www.wineenthusiast.com). In the CSV file, the most interesting column was a description of wines by reviewers like this review of a Napa Valley Cabernet from the Heitz Cellar:

"This tremendous 100% varietal wine hails from Oakville and was aged over three years in oak. Juicy red-cherry fruit and a compelling hint of caramel greet the palate, framed by elegant, fine tannins and a subtle minty tone in the background. Balanced and rewarding from start to finish, it has years ahead of it to develop further nuance. Enjoy 2022–2030."

---

This is a simplified first step toward a total classification or wines based on descriptive characteristics. To this end, we hand selected 50 features (moderately engineered) that we will use to build a binary matrix to train different classification models with. The feature functions can be found in the word_finder_chard.ipynb file. As expected, there are certain words that are excellent predictors of American and French wines. Almost every model tested above expectations on unseen testing data. 

Using an proprietary stacking model, we took weighted votes from seven models: k-nearest neighbors, naive bayes, logistic regression, support vector machines, decision tree, random forest, and an XGBoost model. Random Forest and a heavily manufactured XGBoost outperformed the pack and were given extra voting power. On unseen wine descriptions, our stacked model correctly identified 92.5% of the holdout data with a precision of 0.841 and a recall of 0.865. 

To test the model on your own descriptions, please feel free to download the streamlit files for code to get the data formatted, fit the model, and run the streamlit application. If time permits, the application will be published for everyday use.







