from project.views import custom_page,generate_quote,user_form,form_success_view
from django.urls import path
urlpatterns = [
    path('index/',custom_page,name="render_html"),
    path('quote/',generate_quote,name="quote-generator"),
    path('forms/',user_form,name="forms"),
    path('success/',form_success_view,name="form-success")
]

