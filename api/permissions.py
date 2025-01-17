from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission): 

    def has_object_permission(self, request, view, issue): 

        # Read permissions are allowed to any request, 

        # so we'll always allow GET, HEAD or OPTIONS requests. 

        if request.method in SAFE_METHODS: 

            return True 

        # Write permissions are only allowed to the author of the issue. 

        return issue.author == request.user 