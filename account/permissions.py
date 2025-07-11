from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # print(obj,obj.owner.username,request.user.username)
        return obj.owner == request.user



class MembersPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.user.id)
        return obj.members.filter(id=request.user.id).exists()


class AssignedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user)
        print(obj.assign_to)

        return obj.assign_to.id == request.user.id



class MemberTaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.user)
        # print(obj.project.members.filter(id=request.user.id))
        if request.method in permissions.SAFE_METHODS:
            return obj.project.members.filter(id=request.user.id).exists()

        return False
