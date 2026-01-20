from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.http import HttpResponse # এটি দরকার
from django.core.management import call_command # এটি দরকার

# ডাটাবেস আপডেট করার জন্য এই বিশেষ ফাংশনটি
def run_migrations(request):
    try:
        call_command('makemigrations')
        call_command('migrate')
        return HttpResponse("Database Updated Successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

urlpatterns = [
    path('run-migrations-now/', run_migrations), # এই লিঙ্কে ক্লিক করলে ডাটাবেস ঠিক হবে
    path('admin/', admin.site.urls),
    path('', include('blood_requests.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
