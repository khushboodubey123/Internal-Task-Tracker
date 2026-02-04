ROLE_MEMBER = 'member'
ROLE_ADMIN = 'admin'
ROLE_MANAGER = 'manager'
ROLE_CHOICES = (
    (ROLE_MANAGER, 'Manager'),
    (ROLE_MEMBER, 'Member'),
)
PENDING = 'pending'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_DONE = 'done'

STATUS_CHOICES = (
    (PENDING, 'pending'),
    (STATUS_IN_PROGRESS, 'In Progress'),
    (STATUS_DONE, 'Done'),
)