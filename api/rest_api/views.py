from .serializers import CourseSerializer, CourseCodeSerializer, LectureSerializer, PrerequisiteSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import Course, CourseCode
from scheduler.models import Schedule
from scheduler.views import is_available


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        code = kwargs['course_code']
        course_code = get_object_or_404(CourseCode, code=code)
        queryset = queryset.filter(course_code=course_code)

        if request.GET.get('code'):
            code = request.GET['code']
            queryset = queryset.filter(code=code)

        data = [(self.get_serializer(query).data, query) for query in queryset]

        response_data = []

        for serializer, query in data:
            serializer['lectures'] = LectureSerializer(query.lecture_set.all(), many=True).data
            serializer['prerequisites'] = PrerequisiteSerializer(query.prerequisites.all(), many=True).data
            response_data.append(serializer)

        return Response(response_data)


class CourseSearchAPIView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()



class CourseDetailAPIView(APIView):
    queryset = Course.objects.all()
    http_method_names = ["post", ]
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        crn = request.data['crn']
        instance = get_object_or_404(Course, crn=crn)
        serializer = CourseSerializer(instance).data
        schedule = get_object_or_404(Schedule, user=request.user)
        available, _ = is_available(schedule.courses.all(), instance)

        if not available:
            serializer['overlaps'] = True

        serializer['lectures'] = LectureSerializer(instance.lecture_set.all(), many=True).data
        serializer['prerequisites'] = PrerequisiteSerializer(instance.prerequisites.all(), many=True).data

        return Response(serializer)



class CourseCodeListAPIView(ListAPIView):
    queryset = CourseCode.objects.all()
    serializer_class = CourseCodeSerializer


