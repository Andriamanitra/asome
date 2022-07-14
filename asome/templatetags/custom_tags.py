from django import template

register = template.Library()

@register.inclusion_tag("asome/comment.html")
def show_comment(comment):
    return {"comment": comment}

@register.inclusion_tag("asome/user_link.html")
def user_link(user):
    return {"user": user}

@register.inclusion_tag("asome/topic_link.html")
def topic_link(topic):
    return {"topic": topic}
