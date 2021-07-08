"""
./manage.py shell
import t
t.c()
"""

from challenges.models import Challenge
def c(): print([c.c_id for c in Challenge.objects.filter(difficulty='Expert')])