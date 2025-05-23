from django.urls import path, include
from .debug_views import debug_join_community

# Add this special debug URL pattern
debug_patterns = [
    path('communities/<slug:slug>/join_debug/', debug_join_community, name='community-join-debug'),
]

