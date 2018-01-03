from .serializers import CourseSerializer, CourseCodeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Course, CourseCode


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        code = kwargs['course_code']
        print(code)
        course_code = get_object_or_404(CourseCode, code=code)
        queryset = queryset.filter(course_code=course_code)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CourseDetailAPIView(RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseCodeListAPIView(ListAPIView):
    queryset = CourseCode.objects.all()
    serializer_class = CourseCodeSerializer


