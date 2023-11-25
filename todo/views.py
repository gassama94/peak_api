from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from .models import Todo, Profile
from .serializers import TodoSerializer, ProfileSerializer, ProfileWithTodosSerializer, TodoWithOwnerProfileSerializer

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileWithTodosSerializer
    lookup_field = 'pk'

# View for listing and creating todos
class TodoListCreateView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

# View for retrieving, updating, and deleting a single todo
class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoWithOwnerProfileSerializer
    permission_classes = [IsAuthenticated]

# View for retrieving profiles along with their associated todos
class ProfileWithTodosView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileWithTodosSerializer
    permission_classes = [IsAuthenticated]

    # Optionally, you can specify the lookup_field to retrieve profiles by a field other than the default 'pk'.
    # lookup_field = 'username'
