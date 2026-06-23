from django import forms
from student_management_app.models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"


# ============================
#   ADD STUDENT FORM
# ============================
class AddStudentForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Password",
        max_length=50,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Address",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    gender = forms.ChoiceField(
        label="Gender",
        choices=gender_list,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    profile_pic = forms.FileField(
        label="Profile Pic",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    # Load dynamic dropdowns
    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)

        # Load courses dynamically
        courses = Courses.objects.all()
        course_list = [(course.id, course.course_name) for course in courses]
        self.fields['course_id'] = forms.ChoiceField(
            label="Course",
            choices=course_list,
            widget=forms.Select(attrs={"class": "form-control"})
        )

        # Load session years dynamically
        sessions = SessionYearModel.objects.all()
        session_list = [
            (session.id, f"{session.session_start_year} to {session.session_end_year}")
            for session in sessions
        ]
        self.fields['session_year_id'] = forms.ChoiceField(
            label="Session Year",
            choices=session_list,
            widget=forms.Select(attrs={"class": "form-control"})
        )


# ============================
#   EDIT STUDENT FORM
# ============================
class EditStudentForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Address",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    gender = forms.ChoiceField(
        label="Gender",
        choices=gender_list,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    profile_pic = forms.FileField(
        label="Profile Pic",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"})
    )

    # Load dynamic dropdowns
    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)

        # Load courses dynamically
        courses = Courses.objects.all()
        course_list = [(course.id, course.course_name) for course in courses]
        self.fields['course_id'] = forms.ChoiceField(
            label="Course",
            choices=course_list,
            widget=forms.Select(attrs={"class": "form-control"})
        )

        # Load session years dynamically
        sessions = SessionYearModel.objects.all()
        session_list = [
            (session.id, f"{session.session_start_year} to {session.session_end_year}")
            for session in sessions
        ]
        self.fields['session_year_id'] = forms.ChoiceField(
            label="Session Year",
            choices=session_list,
            widget=forms.Select(attrs={"class": "form-control"})
        )
