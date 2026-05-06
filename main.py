from Classes.Scrapping_movie import Scraping_movie
from Classes.sentiment import Sentiment
from Classes.visulization import SentimentVisulization

# mady by  << Helmy >>

if __name__ == '__main__' :
    # some rule
    print("Hello user i use your chrome to get some data don't close it and go to terminal to write movie name ")
    # get movie comment
    movie_data = Scraping_movie()
    [title ,comments] = movie_data.get_movie_comment()
    

    # analyze comment && get result
    sentiment_data = Sentiment(comments)
    analyze_result = sentiment_data.analyze
    
    # Visulization
    visul = SentimentVisulization(analyze_result, "  ".join(title.split()))
    