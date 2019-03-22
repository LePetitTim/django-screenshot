from rest_framework import serializers


class ScreenshotSerializer(serializers.Serializer):
    url = serializers.URLField()
    viewport_width = serializers.IntegerField(required=False, initial=1920)
    viewport_height = serializers.IntegerField(required=False, initial=1080)
    selector = serializers.CharField(initial='body', required=False)
    waitfor = serializers.ListField(serializers.CharField(required=True), required=False)
    forward_headers = serializers.JSONField(required=False, initial={})