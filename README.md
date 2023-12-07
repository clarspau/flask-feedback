# Flask-Feedback
This Flask Feedback application allows users to sign up, log in, and manage feedback. Users can register, log in, add feedback, edit their feedback, delete their feedback, and view a list of all feedback they've given. The application emphasizes user authentication, authorization, and feedback management.


### Part 0: Set up your environment
Create a virtual environment (venv) and activate it.
Install the required packages: Flask, Flask-DebugToolbar, Werkzeug, Flask-SQLAlchemy.
Place your code on GitHub.

### Part 1: Create User Model
Create a SQLAlchemy model for the User with columns: username, password, email, first_name, last_name.

### Part 2: Make a Base Template
Add a base template with slots for page title and content. Utilize Bootstrap for simplicity, focusing less on styling.

### Part 3: Make Routes For Users
/: Redirect to /register.
/register: Register a new user.
/login: Provide a login form.
/secret: Display "You made it!" if logged in.

### Part 4: Don’t let everyone go to /secret
Protect /secret route to allow only logged-in users. Store username in the session upon successful login or registration.

### Part 5: Log out users
/logout: Clear session information and redirect to /.

### Part 6: Let’s change /secret to /users/<username>
Change /secret to /users/<username>. Display user information and ensure only logged-in users can access.

### Part 7: Give us some more feedback!
Create a SQLAlchemy model for Feedback. It includes columns: id, title, content, username.

### Part 8: Make/Modify Routes For Users and Feedback
/users/<username>: Display user information and feedback. Allow editing and deleting feedback, and adding new feedback.
/users/<username>/delete: Delete the user and associated feedback. Only the logged-in user can delete their account.
/users/<username>/feedback/add: Display a form to add feedback.
/users/<username>/feedback/add: Add new feedback. Only the logged-in user can add feedback.
/feedback/<feedback-id>/update: Display a form to edit feedback. Only the author can see this form.
/feedback/<feedback-id>/update: Update specific feedback. Only the author can update it.
/feedback/<feedback-id>/delete: Delete specific feedback. Only the author can delete it.

Enjoy building and exploring the Flask Feedback application!
