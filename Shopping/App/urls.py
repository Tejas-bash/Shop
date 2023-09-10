from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),

    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart),

    path('minuscart/', views.minus_cart),

    path('removecart/', views.remove_cart),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',
         form_class=MyPasswordChangeForm, success_url="/passwordchangedone/"), name='changepassword'),

    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password-reset.html',
         form_class=MyPasswordResetForm), name='password-reset'),

    path('password-reset-done', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/password_reset_done.html',), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/passsword_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html',), name='password_reset_complete'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('topwear/', views.Topwear, name='topwear'),

    path('topwear/<slug:data>', views.Topwear, name='topweardata'),

    path('bottomwear/', views.Bottomwear, name='bottomwear'),

    path('bottomwear/<slug:data>', views.Bottomwear, name='bottomweardata'),

    path('laptop/', views.laptop, name='laptop'),

    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),

    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('search/',views.Search_data,name='get_student'),
    path('checkout/', views.checkout, name='checkout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
