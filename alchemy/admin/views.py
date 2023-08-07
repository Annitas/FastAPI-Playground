from sqladmin import ModelView
from users.models import User


class UserAdmin(ModelView, model=User):
    name = "User"
    can_delete = False
    # column_details_exclude_list = [User.gashedpassword]
    icon = "fa-solid fa-user"
    page_size = 10
    column_list = [User.id, User.name]

