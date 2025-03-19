
if "{{ cookiecutter.cms }}" == "DjangoCMS":
    from cms.utils.page import get_page_from_request
    from cms.views import details
    #
    # This needs a CMS page with a "404" slug.
    #
    def custom_404(request, exception):
        if hasattr(request, "_current_page_cache"):  # we'll hit the cache otherwise
            delattr(request, "_current_page_cache")
        page = get_page_from_request(request, "404")
        request.current_page = page  # templatags seem to use this.
        response = details(request, "404")  # the main cms view
        if hasattr(response, "render"):  # 301/302 dont have it!
            response.render()  # didnt know about this, but it's needed
        response.status_code = 404  # the obvious
        return response

if "{{ cookiecutter.cms }}" == "Wagtail":
    from django.shortcuts import render
    from django.http import HttpResponseNotFound
    from wagtail.models import Page
    #
    # This needs a Wagtail page with a "404" slug.
    #
    def custom_404(request, exception):
        try:
            page = Page.objects.get(slug="404")
            request.site = page.get_site()
        except Page.DoesNotExist:
            return HttpResponseNotFound("404 page not found")
        
        response = render(request, page.specific.get_template(request), {"page": page})
        response.status_code = 404
        return response