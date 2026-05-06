from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

class Sentiment:

    def __init__(self, comments: list[str]) :
        # to explain the class
        self.about_sentiment()
        self.comments = comments
        # to create an object of the SentimentIntensityAnalyzer class to use its methods
        self.analyzer = SentimentIntensityAnalyzer()
        #  to check if the vader lexicon is downloaded
        self.check_nltk()
        # to create a dictionary to store the number of positive, negative and neutral comments
        self.analyze = {
            "positive": 0,
            "negative": 0,
            "neutral": 0
        }
        # to analyze the sentiment of the comments and store the result in the analyze dictionary
        self.set_analyze(self.analyze_sentiment())
    
    # About class
    def about_sentiment(self) -> None:
        print("<< this class is about analyzing the sentiment of the comments >>")
        print("we will use the vader library to analyze the sentiment of the comments")
        print("=" * 50)
    
    # to search of vader library in your pc or install
    def check_nltk(self) -> None:
        try :
            nltk.data.find('sentiment/vader_lexicon.zip' or 'sentiment/vader_lexicon')
            print("vader lexicon is already downloaded")
        except LookupError :
            print("downloading vader lexicon...")
            nltk.download('vader_lexicon')
    
    # to analyze the sentiment of the comments
    def analyze_sentiment(self) -> list[dict[str, float]] :
        sentiments = []
        for comment in self.comments :
            # to get the comment score 
            sentiment = self.analyzer.polarity_scores(comment)
            sentiments.append(sentiment)
        return sentiments
   
    # to set the analyze dictionary with the number of positive, negative and neutral comments
    def set_analyze(self, sentiments: list[dict[str, float]] ) -> None:
        for sentiment in sentiments :
            if sentiment['compound'] >= 0.05:
                self.analyze['positive'] += 1
            elif sentiment['compound'] <= -0.05:
                self.analyze['negative'] += 1
            else:
                self.analyze['neutral'] += 1

# test = Sentiment(["I love this movie", "I hate this movie", "This movie is okay"])
# print(test.analyze)