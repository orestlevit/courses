Catalog of books made on DRF (Django Rest Framework).

Installation: 
                    
                    Linux - Terminal in PyCharm 
		                1.1 pip install django
		                1.2 pip install djangorestframework
		                1.3 pip install django-cors-headers
		                1.4 python manage.py makemigrations
		                1.5 python manage.py migrate
		                1.6 python manage.py createsuperuser
	
                   Download the application for API testing: For example: "Insomnia"
                    2.1 https://insomnia.rest/download
               
Setting up Insomnia:

3.1 Change method:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_16-49.png)
       	       3.2 Enter: http://127.0.0.1:8000/api-auth-token/
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_16-52.png)
       	       3.3 Change on JSON:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_16-53.png)
       	       3.4 Enter your data(username and password that you specified in paragraph 1.6):
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_16-55.png)
       	       3.5 Press Send:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_16-55_1.png)
       	       3.6 You will receive your token:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-02.png)
       	       3.7 Save this token
               
  3.8 Go to headers tab and click add:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-04.png)
       	       3.9 Enter as in the picture:
               ![Setting up Insomnia](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-08.png)
       	       3.10 Now you can use the program. 
               
               
  Usage:
        	    
             
  If you want to add new Author: 
1. Change method on POST
                    
2. Enter: http://127.0.0.1:8000/api/authors/

3. Enter as in the picture:
   
  ![Usage](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-35.png)

4. Press Send
        				    
  If you want to see all authors: 
1. Change method on GET
2. Enter: http://127.0.0.1:8000/api/authors/
3. Press Send
        	
  If you want to change the title of the author: 
1. Change method on GET
2. Enter: http://127.0.0.1:8000/api/authors/
3. Choose the id of the author you want to change:
   
  ![Usage](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-36.png)
  
4. Enter: http://127.0.0.1:8000/api/authors/ID OF AUTHOR FOR CHANGE/
5. Change method on PATCH
6. Enter as in the picture:

  ![Usage](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_18-25.png)
  
7. Press Send
        				    
  If you want to add new Book: 
1. Change method on POST
2. Enter: http://127.0.0.1:8000/api/books/
3. Enter as in the picture:
   
  ![Usage](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_17-44.png)

4. Press Send
        				    
  If you want to see all books: 
1. Change method on GET
2. Enter: http://127.0.0.1:8000/api/books/
3. Press Send
        	
If you want to change something in the Book: 
1. Change method on GET
2. Enter: http://127.0.0.1:8000/api/books/ID OF BOOK FOR CHANGE/
3. Choose the id of the book you want to change
4. Change method on PATCH
5. Enter as in the picture:
   
  ![Usage](https://github.com/orestlevit/BookCatalogDRF/blob/master/Image/2023-07-19_18-24.png)
  
6. Press Send
        				    
           The results of all actions will be visible in the window on the right.			    
        				    
       	
       	       
       	       
		
	
	       
	
		
		
		
		
	
		      
		      
		      
