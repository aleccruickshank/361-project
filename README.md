# 361-project

Communication Contract

Requesting Data:
	
	The REST API can be accessed through HTTP requests and responses in JSON format. All requests must be in the object format { key: value}. The two keys needed for this microservice are:

		username
		password

An example object would look like this:

	{ username: “user1”, password: “password1” }

All functionality can be accessed through GET, POST, PUT, and DELETE methods.

The two routes to access are (with an example localhost):

	http://127.0.0.1:5000/validate

	http://127.0.0.1:5000/users

Validate:


	This route only supports a POST method, a username and password can be passed to it as a JSON object, it will return a boolean value if the credentials are valid or not. 

Users:

	This route supports GET, POST, PUT, and DELETE methods. 

	GET: Returns the dictionary of all users.

	POST: Passing an object with both a username and password will update the password for the given username.

	PUT: Passing an object with both a username and password will create a new user for the given credentials, if it does not already exist.

	DELETE: Passing an object with only a username, will remove that user from the dictionary of users.
  
  ![Untitled-1](https://user-images.githubusercontent.com/97071456/236998754-33abec20-ae71-494c-ba71-9f8feaeaaeb9.png)
