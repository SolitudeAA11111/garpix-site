from garpixcms.urls import *  # noqa

urlpatterns = [
    path('dev/api/', include('modelthreed.urls'))
] + urlpatterns
