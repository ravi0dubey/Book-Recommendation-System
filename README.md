# Book-Recommendation-System

Types of Recommendation Systems
1.	Popularity-based recommendation system
Popular or best books are shown in the system. It is based on the formula.

2.	Collaborative Filtering
The collaborative filtering method is based on gathering and analyzing data on users’ behavior. This includes the user’s online activities and predicting what they will like based on their similarity with other users.
For example, if user A likes Apples, bananas, and Mango while user B likes Apple, Banana, and Jackfruit, they have similar interests. So, it is highly likely that A would like Jackfruit and B would enjoy Mango. This is how collaborative filtering takes place.

3.	Content-Based Filtering

Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. 

For instance, if a user likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero genre or films describing Tony Stark. The central assumption of content-based filtering is that you will also like a similar item if you like a particular item.

4.	Hybrid Recommendation Systems

In hybrid recommendation systems, products are recommended using Popularity based, Content-based, and collaborative filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming and is said to provide more accurate recommendations than other recommender systems.
## Popularity Based Recommender System
Top 50 books wwith highest average rating but should have minimun 250 ratings

## Collaborative Based Recommender System
We will create a table using books and rating dataset with books in row and users in columns and what is the rating given by the user </br>
Criteria We are not going to choose all users and books
1. only those users who has given atleast ratings to 200 books </br>
2. but only those books who has got 50 ratings atleast or popular 50 books </br>
![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/0aada47d-0e52-4ff5-93a4-f56cd2ba3fca)
