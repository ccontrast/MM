from myapp.models import UserProfile
from django.http import HttpResponse

"""conserve code
think now
"""

"""ask questions"""

def index(request):
  profile_list = UserProfile.objects.all()
  output = ', '.join([p.user for p in profile_list])
  return HttpResponse(output)

def detail(request, user_id):
  return HttpResponse("User ID: %s" % user_id)
