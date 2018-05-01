from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class MyApphook(CMSApp):
    app_name = "blog"
    name = _("BLOGAPP")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog.urls"]       # replace this with the path to your application's URLs module