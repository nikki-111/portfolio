from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = [
            {"name": "Data Analytics", "description": "Extract insights from your data using Python libraries like Pandas, NumPy, and Matplotlib."},
            {"name": "Creating Dashboards", "description": "Build interactive and visually appealing dashboards using tools like Plotly, Dash, and Tableau."},
            {"name": "Dynamic Websites", "description": "Develop dynamic and responsive websites using Python frameworks like Django and Flask."},
            # {"name": "Automation Scripts", "description": "Create custom automation scripts to streamline repetitive tasks and improve efficiency."},
            # {"name": "API Development", "description": "Design and develop RESTful APIs for seamless integration between applications."},
            # {"name": "Machine Learning Solutions", "description": "Implement machine learning models to solve complex business problems."},
        ]
        context['works'] = RecentWork.objects.all()
        return context
