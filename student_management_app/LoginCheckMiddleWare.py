from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):

        user = request.user
        raw_path = request.path
        path = raw_path.rstrip("/")

        public_urls = [
            reverse("login").rstrip("/"),
            reverse("doLogin").rstrip("/"),
            reverse("logout").rstrip("/"),
        ]

        # Allow static files
        if raw_path.startswith("/static/"):
            return None

        # If user is NOT logged in
        if not user.is_authenticated:
            if path not in public_urls:
                return redirect("login")
            return None

        # Allow logout for logged-in users
        if path == reverse("logout").rstrip("/"):
            return None

        module_name = view_func.__module__

        # HOD
        if user.user_type == 1:
            if raw_path.startswith("/admin"):
                return None
            if "HodViews" not in module_name:
                return redirect("admin_home")

        # Staff
        elif user.user_type == 2:
            if "StaffViews" not in module_name:
                return redirect("staff_home")

        # Student
        elif user.user_type == 3:
            if "StudentViews" not in module_name:
                return redirect("student_home")

        return None
