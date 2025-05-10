from django.template import Library

register = Library()

@register.simple_tag
def total_tasks(user):
    return f'{user.tasks.count()} total tasks'

@register.simple_tag
def total_done(user):
    return f'{user.tasks.filter(state='Done').count()} total tasks done'

@register.simple_tag
def total_undone(user):
    return f'{user.tasks.filter(state='Undone').count()} total tasks undone'

@register.simple_tag
def total_in_progress(user):
    return f'{user.tasks.filter(state='In progress').count()} total tasks in porgress'

# @register.simple_tag
# def latest_created_tasks(user):
#     return user.tasks.order_by('-created')[:2]

# @register.simple_tag
# def latest_updated_tasks(user):
#     return user.tasks.order_by('-updated')[:2]
