from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from models import Profile, Call, Skill, Resource

urlpatterns = patterns('',
    #url(r'^/', 'views.index'),

    url(r'^chamada/$', ListView.as_view(model=Call,
                                       context_object_name='calls',
                                       template_name='volunteers/calls/index.html'),
        name="calls-list"),
    url(r'^chamada/(?P<slug>[-\w_]+)/', DetailView.as_view(model=Call,
                                                        context_object_name='call',
                                                        template_name='volunteers/calls/detail.html'),
        name='call-detail'),

    #url(r'^chamada/cadastro/', 'views.call.new'),

    #url(r'^perfil/', 'views.profile.index'),
    #url(r'^perfil/(?P<year>\d+)/', 'views.profile.details'),
    #url(r'^perfil/cadastro/', 'views.profile.new'),
)
