from flask import Flask,render_template,request
import pickle
import numpy as np

#Loading dataset generated from jupyter notebook

popular_50_books_df = pickle.load(open('popular_50_books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    print(f"book-title : {list(popular_50_books_df['Book-Title'].values)}")
    print(f"book-author : {list(popular_50_books_df['Book-Author'].values)}")
    print(f"image: {list(popular_50_books_df['Image-URL-S'].values)}")
    print(f"avg_Rating : list(popular_50_books_df['avg_ratings'].values)")

    return render_template('index.html',
                           book_name = list(popular_50_books_df['Book-Title'].values),
                           author=list(popular_50_books_df['Book-Author'].values),
                           image=list(popular_50_books_df['Image-URL-S'].values),
                           votes=list(popular_50_books_df['num_ratings'].values),
                           rating=list(popular_50_books_df['avg_ratings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    recommended_data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        print(f"temp_Df : {temp_df}")
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-S'].values))

        recommended_data.append(item)

    print(recommended_data)

    return render_template('recommend.html',data=recommended_data)

if __name__ == '__main__':
    app.run(debug=True)