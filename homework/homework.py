import pdf_code
import pandas

df = pandas.read_csv('articles.csv', dtype={'id': str})


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df['id'] == self.article_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.article_id, 'price'].squeeze()

    def available(self):
        available_number = df.loc[df['id'] == self.article_id, 'in stock'].squeeze()
        # if available_number > 0:
        #     return True
        # else:
        #     return False
        return available_number

    def reduce_quantity(self):
        df.loc[df['id'] == article.article_id, 'in stock'] = df.loc[df['id'] == article.article_id, 'in stock'] - 1
        df.to_csv('articles.csv', index=False)


class Pdf:
    def __init__(self, article_object):
        self.article_object = article_object

    def print_pdf(self):
        pdf_code.print_pdf(self.article_object.article_id, self.article_object.name, self.article_object.price)


print(df)
article_id_number = input('Choose an article to buy: ')
article = Article(article_id_number)
if article.available():
    # if return 0 == False
    pdf = Pdf(article)
    pdf.print_pdf()
    article.reduce_quantity()



