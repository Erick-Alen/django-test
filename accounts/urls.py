from django.urls import path
from accounts.views import AccountView, AccountDetailView

# if param type are isn't informed, string is defined by default
urlpatterns = [
    path("accounts/", AccountView.as_view(), name="Account view"),
    path(
        "accounts/<int:account_id>",
        AccountDetailView.as_view(),
        name="Account detail view",
    ),
]
