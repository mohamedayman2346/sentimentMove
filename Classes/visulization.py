import matplotlib.pyplot as plt

class SentimentVisulization :

    def __init__(self, sentiment_data: dict[str, int], movie_name: str) -> None :
        self.data = sentiment_data
        self.movie_name = movie_name
        self.colors = ['#27ae60', '#c0392b', '#7f8c8d']
        self.display_pie_chart()
    
    # show result in circle
    def display_pie_chart(self, movie_name: str = 'movie') -> None :
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        # check of data
        if not self.data or sum(sizes) == 0 :
            print('No data to visualization!')
            return

        plt.figure(figsize=(10, 7))
        explode = (0.1, 0, 0)

        plt.pie(
            sizes,
            explode = explode,
            labels = labels,
            colors = self.colors,
            autopct = '%1.1f%%',
            shadow = True,
            startangle = 140
        )

        plt.title(f"Sentiment Analysis Result for : {self.movie_name}", fontsize = 15, pad = 20)
        plt.axis("equal")
        plt.show()
        print("The program finished succesfully")
