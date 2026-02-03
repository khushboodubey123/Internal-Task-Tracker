# Internal Task Tracker – Django REST API
# Problem Understanding

The goal of this project is to build a **small internal task tracking system** using Django and Django REST Framework.

The application will allow a team to:
- Create tasks
- Assign tasks to users
- Update task status
- Track task progress within the organization

This system is intended for **internal use**, not public users, and focuses on clean API design, proper data modeling, and maintainable code structure.


# Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Version Control:** Git, GitHub
- **Language:** Python 3

# Assumptions

- Users are internal team members 
- Authentication will be handled using Django’s built-in User model
- Each task:
  - Has a title, description, status, priority
  - Is assigned to one user
  - Is created by one user
- Task statuses will be predefined (e.g., `Pending`, `In Progress`, `Completed`)


# Project Approach (High Level)

1. Design database models for Users and Tasks
2. Expose REST APIs using Django REST Framework
3. Implement CRUD operations for tasks
4. Add authentication and permissions
5. Ensure clean project structure and Git practices
6. Focus on readable, maintainable, and scalable code

# Weekly Development Plan

Day 1 – Planning & Setup
- Create Django project
- Initialize Git repository
- Set up virtual environment
- Create `.gitignore` and `requirements.txt`
- Write README with problem understanding and plan

Day 2 – Models & Database Design

- Create Task model
- Define fields (title, description, status, assigned_to, created_by)
- Run migrations
- Register models in Django admin

Day 3 – REST API Development
- Create serializers
- Implement CRUD APIs for tasks
- Use ViewSets / APIViews
- Test APIs using Postman

Day 4 – Authentication & Permissions
- Integrate user authentication
- Restrict task access based on user
- Ensure only authorized users can modify tasks

Day 5 – Enhancements & Cleanup
- Add filtering and ordering
- Improve validation
- Refactor code
- Add comments and documentation

