from rest_framework.permissions import BasePermission


# class ViewPerm(BasePermission):
#
#     def has_permission(self):
#         if self.action == 'create':
#             self.permission_classes = [IsAuthenticated, ~IsStaff]
#         #     return request.user.is_authenticated() is not request.user.is_staff
#         elif self.action in ['retrieve', 'update', 'list']:
#             self.permission_classes = [IsAuthenticated, IsAuthor|IsStaff]
#         #     return request.user == view.get_object().is_author or request.user.is_staff
#         elif self.action == 'destroy':
#             self.permission_classes = [IsAuthenticated, IsAuthor]
#         #     return request.user == view.get_object().is_author
#         return [permission() for permission in permission_classes]


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='staff').exists():
            return True
        return False


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().is_author
