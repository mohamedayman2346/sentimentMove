from Classes.scraping import Scraping 

class Scraping_movie:

    def __init__(self) :
        self.about_project()
        self.page_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
        # to create an object of the Scraping class to use its methods
        self.scraping = Scraping("https://www.imdb.com/")
        self.check_site()

    # to explain the project
    def about_project(self) -> None:
        print("<< this project is about scraping the comments of the movies and analyzing their sentiment >>")
        print("we will use the IMDB website to scrape the comments")
        print("we will use the selenium library to scrape the comments")
        print("we will use the vader library to analyze the sentiment of the comments")
        print("=" * 50)
    
    # to check if we are in the right website
    def check_site(self) -> None:
        self.scraping.check_site(self.page_title)
    
    # to get the comments of the movie
    def get_movie_comment(self) -> list[str]:
        movie_name = input("enter the movie name: ").strip()
        try :
            search = self.scraping.get_element("imdb-header-search__input")
            self.scraping.send_keys_to_search_bar(search, movie_name)
            first_result = self.scraping.get_element("ipc-lockup-overlay")
            self.scraping.Click_element(first_result)
            title = self.scraping.get_element("sc-af040695-0")
            comments = self.scraping.get_elements("ipc-html-content-inner-div")
            # to return the text of the comments in a list
            return [title.text ,list(map(lambda comment: self.scraping.get_element_text(comment), comments))]
        except Exception as e :
            print(f"the error is {e}")
    


# movie = Scraping_movie()
# movie.check_site("IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows")

# [title, comments] = movie.get_movie_comment()
# print(title)
# print(comments)
# for comment in comments :
#     print(comment.text)