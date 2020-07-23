from django.db.models import Count
from fb_post.models import Reaction

from fb_post.decorators import decorators

# 7
@decorators
def get_total_reaction_count():
    reaction_count_dict = Reaction.objects\
                                  .aggregate(
                                      count=Count('reacted_by')
                                  )

    return reaction_count_dict
