# Project Requirements

I was tasked to create a CLI app to log and track orders for a pop-up café owner that delivers food and drinks to local offices. Their requirements were as follows:

-  The client wants to have a store of products, couriers and orders, and modify/view them using basic CRUD operations.
- The client wants this data to be persisted such that all changes made in prior sessions are maintained.
- The order wants all of the persisted data to be loaded upon start-up.
- The client requires a robust, well-tested app.
- The client wants the app to have frequent updates.

The way I tackled this business problem was to spend a week focusing on a specific aspect of the requirement, and to gradually increase the number of requirements covered by my program. As I am knew to Python, this project has allowed me to implement the things that I have learnt, as I learnt them, in the hopes of with time, meeting all client requirements.

# Week 1:

My focus for the first week was to flesh out the user interface for the main menu and product menu, as well as satisfy these core functionalities:

- The addition of products.
- Printing of products.
- Updating products.
- Deletion of products.

![image](https://user-images.githubusercontent.com/115266421/203516622-aa71f382-4734-43ed-9180-5a56c6ef1eb7.png)



### Advantages:

- It was very straightforward to implement this code, and it acted as proof-of-concept for the product CRUD operations

### Disadvantages:

- Doesn't reflect the business model very well, as a lot of Python-based jargon will have to be explained in order to get the client to understand how the app meets their requirements.

# Week 2:

These core functionalities were introduced:

- Inclusion of a courier menu.
- Add courier.
- Print couriers.
- Update courier.
- Delete courier.
- Save products and couriers to txt files.


![image](https://user-images.githubusercontent.com/115266421/203517565-7ec0d5b5-34e5-40ac-abc7-6b85873ce1a7.png)

### Advantages:

- Included some more functionality for couriers
- Data is now persisted and can be loaded from file upon starting the program.
- Still a very simple model

### Disadvantages:

- Program logic still doesn't explain the business model very well.
- Data was persisted to file after every CRUD operation was completed. Files were read and wrote to many times, makes losing file data more likely.
- Logic to do with data persistence is coupled to both the user interface layer, and business logic layer. This makes updating the codebase very difficult.

# Week 3:

These core functionalities were introduced:

- Print orders
- Add orders
- Update order
- Delete order

![image](https://user-images.githubusercontent.com/115266421/203523251-a27dd5af-b937-4799-b642-d4e7f383ff6e.png)


### Advantages:

- CRUD operations for products, orders and couriers have been included.
- Still very simple implementation

Disadvantages:

- Orders had yet to be persisted - core functionality of data persistence had yet to be fully implemented
- My program was not extensible, major refactoring had to occur in order to gradually increase the number of requirements met.
- Still not reflecting the business model very well

## Introduction of testing:

It was at this point that the concepts of unit testing were introduced to me, so I tried to implement this in my project. However I ran into some serious issues. All of my functions had several responsibilites, from taking input and then editing in-memory list, to writing these changes to file. My functions were long, ugly, confused and I had no idea on how to test them. This led me down the rabbit hole of a design structure that could help me write extensible code

## Repository pattern... INCOMING!

I had taken some advice and looked into some design patterns that may help me... which led me to the book 'Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices' by Harry Percival and Bob Gregory. This included a section on something called the 'repository pattern'.

![image](https://user-images.githubusercontent.com/115266421/203539815-0c9b6537-5272-47c9-8d22-c1734fb18b8a.png)


If done right, and including the concept of dependency inversion, my business logic layer would not need to change if the persistence layer changes. I however, couldn't grasp where in my programs all the function responsibilites should be. Also, I did not know how to design my project using dependency inversion. My project was further impeded by my lack of ability in the implementation of OOP principles. I struggled to test all of my classes and mock the dependencies correctly.

## Advantages:
- Data persistence is abstracted away so clients do not have to focus on such lower-level details
- Better simualation of the business problem - I was able to use more subject-matter terminology in the explanation of my Product class.

## Disadvantages:
- I introduced a lot of complexity in my program - a complexity that paralysed me and left me unable to model the problem, nor test me.


After several tries to get my program, based on the repository pattern, to work... it had to be shelved.

# Week 4:

I decided to completely remove any OOP aspects from my program, to keep the my project as simple as possible in my implementation. Due to my not so brief affair with the repository pattern I had very little time to redesign my program and make sure that all key requirements were met. 

# Project design
![image](https://user-images.githubusercontent.com/115266421/203532583-146d98ae-9745-4e82-b8d0-3b40c3669752.png)

I feel like this new structure struck a good balance between simplicity and the benefits of abstraction. I don't want to bombard a potential client with programming-specific concepts when it's not necessary to do so.

# Project design - tree structure


![image](https://user-images.githubusercontent.com/115266421/203539145-b6c82cee-b758-4103-848f-a02a230ea2a4.png)

## Advantages:

- Simple implementation
- Data is fully persisted to csv files - allowing for easier storage of multidimensional data and the in-memory storage of data as dictionaries, which are very easy to change.
- Employing a three-layered program makes it easy to abstract information from the reader that is unimportant

### UI layer code sample:
![image](https://user-images.githubusercontent.com/115266421/203536787-0d3cf3b3-5751-4b92-9d16-c8bc2fda0327.png)

### Business layer code sample:
![image](https://user-images.githubusercontent.com/115266421/203536964-e39d4989-ef93-42a9-8976-2ae4ae045fab.png)

### Persistence layer code sample:
![image](https://user-images.githubusercontent.com/115266421/203537769-4d6efd69-90f2-4e28-8c86-b031583df25c.png)



## Disadvantages:

- Due to time constraints, there is very poor test coverage. 
- Slightly worse reflection of the business model

# Week 5 and 6:

The client requires the addition of database functionality - they would like all data to be persisted to a database. This was not achieved due to time-constraints.

# Guaranteeing client requirements - testing:

This was a major issue for me. When starting from scratch from the week 4 requirements, I initially used a test-driven development (TDD) approach. This means that my tests precluded any actual code being written, and that I could be sure of my code working when I ran my program. I ran into many hurdles, the first being issues with pytest imports. I had to restructure my file organisation in the root directory to patch this issue in the short-term. I also faced serious issues with ensuring I had a working program before the deadline.

Unfortunately, I had to trade the robustness of my program for a program that has CRUD functionalities for each object of interest.


# Reflections:

Due to the lack of testing, in a real business situation, I would advocate for more time to make sure the program is robust.
I don't think it wrong to be ambitious and to aim to present the best program I can conjure up, however in future I will be mindful to not make such big changes so close to a hard deadline.

I would love to have another go in future at implementing repositories, to allow for a seamless transition to database inclusion.









