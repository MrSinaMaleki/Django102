# Django Blog Platform Project

## Project Overview
This project is designed to help you build a simple yet functional blog platform using Django. It aims to solidify your understanding of Django's core functionalities, particularly its Model-View-Template (MVT) architecture. You will develop a blog that allows users to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

## Core Requirements
Your blog should meet the following requirements:

### 1. Post Model
Create a `Post` model within your Django application with the following fields:
- **title**: String field for the blog post title.
- **description**: Text field for the blog post content.
- **author**: String field for the author's name.
- **created_at**: DateTime field to automatically store the time of creation.
- **updated_at**: DateTime field to automatically update when a post is modified.

### 2. CRUD Functionality
Implement CRUD functionalities for your blog posts using functional views:
- **Create**: A view and form to add new posts.
- **Read**: Views to display a list of posts and a detailed view for individual posts.
- **Update**: A view and form to edit existing posts.
- **Delete**: A view to delete posts with a confirmation step.

### 3. URLs Configuration
Set up your URL patterns in `urls.py` inside your blog app and include it in your project's main `config/urls.py`.

### 4. Django Template Language (DTL)
Utilize Django’s Template Language for dynamic content rendering in templates. Employ template tags for loops, conditionals, and data display, ensuring dynamic and responsive user interfaces.

## Optional Extensions
Enhance your blog and further your understanding of Django by implementing the following features:

### 1. Template Inheritance
Use Django’s template inheritance to maintain a consistent layout across your app. Create a base template that includes the common structure and elements.

### 2. Tailwind CSS for Styling
Use Tailwind CSS to style your blog for a modern and responsive design.

### 3. Model Validation
Add custom validators to your model fields to ensure data integrity, such as validating the length of the blog post titles or the format of the author's name.

### 4. Verbose Name and Database Indexes
- Utilize `verbose_name` in your model fields to provide more readable names in the Django admin.
- Use `db_index=True` on important fields to improve query performance.

### 5. Image Field
Add an image field to your `Post` model to allow image uploads and display these images in post details.

### 6. Template Tags
Create custom template tags or filters in a `templatetags` directory to add more functionality to your templates.

## Roadmap for Improvement
- **Beginner**: Focus on the basic CRUD operations and understanding the MVT architecture.
- **Intermediate**: Implement basic styling with Tailwind CSS and start exploring Django Template Language in depth.
- **Advanced**: Dive into creating custom template tags, advanced image handling, and optimizing your models with database indexes.

## Conclusion
This project is a great way to get hands-on experience with Django while building a functional web application. Completing the core requirements will give you a basic blog platform, and the optional extensions will challenge you to explore more complex features and best practices in Django development.
