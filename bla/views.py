from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    if len(request.GET.values()) >= 1:
        import pdb; pdb.set_trace()
        pass

    return {'project': 'bla'}


# Clasa baza de date
# Clasa pentru TODO
# 1 functie pentru introducerea datelor in baza de date
# 1 pentru citirea datelor din baza de date


# class TODO(object):
#     self.CheieUnica = CheieUnica
#     self.Todo = Todo
#     self.status = status
