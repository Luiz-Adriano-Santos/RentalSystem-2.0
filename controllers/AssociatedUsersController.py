from views.UserEditView import EmployeeUserEditView
from views.RegisterAssociatedUserView import RegisterAssociatedUserView
from views.UsersView import UsersView


class AssociatedUsersController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def associated_users_page(self, user):
        # TODO Andreszinho: add get_all_associated_users() method in User class ou algo do tipo XD
        associated_users = user.get_all_users()
        is_associated_users = True
        self.view = UsersView(self, user, associated_users, is_associated_users, )
        self.view.mainloop()

    def create_associated_user_view(self, user):
        self.view.root.withdraw()
        self.view = RegisterAssociatedUserView(self, user)
        self.view.mainloop()

    def return_guest_home(self, user):
        self.view.root.withdraw()
        self.controller.guest_page(user)

    def create_associated_user(self, user):
        # TODO Andreszinho: add create_associated_user() method in User class ou algo do tipo XD
        pass

    def delete_user(self):
        # TODO Andreszinho: implement this method
        pass

    def open_associated_user_edit_page(self, logged_user, user):
        self.view.root.withdraw()
        self.view = EmployeeUserEditView(self, logged_user, user, is_associated_user=True)
        self.view.mainloop()
