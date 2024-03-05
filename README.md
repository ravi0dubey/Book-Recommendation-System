# Book-Recommendation-System

Types of Recommendation Systems
1.	Popularity-based or Rank-based recommendation system
Popular or best books are shown in the system. It is based on the formula.
This kind of recommendation system is useful when we have **cold start** problem. Cold start refers to the issue when we get a new user into the system and the machine is **not** able to recommend books to the user, as the user did not have any historical interactions available in the dataset. In those cases, we can use a popular or rank-based recommendation system to recommend movies to the new user.

3.	Collaborative Filtering
The collaborative filtering method is based on gathering and analyzing data on users’ behavior. This includes the user’s online activities and predicting what they will like based on their similarity with other users.
For example, if user A likes Apples, bananas, and Mango while user B likes Apple, Banana, and Jackfruit, they have similar interests. So, it is highly likely that A would like Jackfruit and B would enjoy Mango. This is how collaborative filtering takes place.

4.	Content-Based Filtering

Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. 

For instance, if a user likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero genre or films describing Tony Stark. The central assumption of content-based filtering is that you will also like a similar item if you like a particular item.

4.	Hybrid Recommendation Systems

In hybrid recommendation systems, products are recommended using Popularity based, Content-based, and collaborative filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming and is said to provide more accurate recommendations than other recommender systems.

## Popularity Based Recommender System
Top 50 books wwith highest average ratings will be displayed on home screen. Each book should have minimun 250 ratings </br>
![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/944028b2-bf7c-451f-990b-f455b92f5e65)

## Collaborative Based Recommender System
We will create a table using books and rating dataset with books in row and users in columns and what is the rating given by the user </br>
Criteria We are not going to choose all users and books
1. only those users who has given atleast ratings to 200 books </br>
2. only those books who has got 50 ratings atleast or popular 50 books </br>
![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/20678e54-aa9d-41ba-aed7-51df2f920ca5)
3. Use **cosine similarity** function between the books and users. Internally consine similarity works as mentioned below </br>
   Books-user pair which has many things in common will have lesser angle hence larger cosine value, while the ones with lesser similarity will be having greater angle and hense lesser cosine value</br>
   i.e cos 0 = 1, cos 45 = .71, cos90 = 0</br>
   
   ![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/8eb19915-1de9-4873-82d1-e782bc036d24) </br>


  Below snapshot shows the recommendation of 5 books based on book entered </br>
![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/3517ed64-ba68-4929-82ef-9d917816f36e) </br>

![image](https://github.com/ravi0dubey/Book-Recommendation-System/assets/38419795/fb8a3d61-aac9-4bdd-84b3-28fbeaf53474)


