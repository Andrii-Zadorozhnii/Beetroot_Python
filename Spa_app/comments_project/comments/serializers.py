import bleach, io, os
from rest_framework import serializers
from .models import Attachment, Comment, Captcha
from PIL import Image
from django.core.files.base import ContentFile


ALLOWED_TAGS = ['a','code','i','strong']

ALLOWED_ATTRIBUTES = {'a':['href','title']}

class CommentSerializer(serializers.ModelSerializer):
    captcha_key = serializers.CharField(write_only=True)
    captcha_text = serializers.CharField(write_only=True)
    replies = serializers.SerializerMethodField()
    attachments = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    def validate_text(self, value):
        cleaned = bleach.clean(
            value,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=True
        )
        return cleaned

    def validate(self, data):
        try:
            captcha = Captcha.objects.get(key=data['captcha_key'])
        except Captcha.DoesNotExist:
            raise serializers.ValidationError({'captcha': 'Invalid CAPTCHA key.'})

        if captcha.text.lower() != data['captcha_text'].lower():
            raise serializers.ValidationError({'captcha': 'Incorrect CAPTCHA.'})

        captcha.delete()
        return data

    def create(self, validated_data):
        validated_data.pop('captcha_key')
        validated_data.pop('captcha_text')
        files = validated_data.pop('attachments', [])

        request = self.context.get('request')
        if request:
            validated_data['user_ip'] = request.META.get('REMOTE_ADDR')
            validated_data['user_agent'] = request.META.get('HTTP_USER_AGENT')


        comment = Comment.objects.create(**validated_data)

        for file in files:
            Attachment.objects.create(comments=comment, file=file)

        return comment

    def get_replies(self, obj):
        replies = obj.replies.all().order_by('-created_at')
        serializer = CommentSerializer(replies, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = Comment
        fields = [
            'id', 'parent', 'username', 'email', 'homepage',
            'text', 'created_at', 'captcha_key',  'captcha_text', 'replies','attachments'
        ]


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Attachment
        fields = ['id', 'file', 'uploaded_at']

    def validate_file(self,file):
        ext = os.path.splitext(file.name)[1].lower()

        if ext in ['.jpg', '.jpeg', '.png', '.gif']:
            file.seek(0)
            try:
                image = Image.open(file)
            except IOError:
                raise serializers.ValidationError('Invalid image file.')

            if image.width > 320 or image.height > 240:
                output = io.BytesIO()
                image.thumbnail((320,240))
                image.save(output,format=image.format)
                file = ContentFile(output.getvalue(),name=file.name)
            return file

        elif ext == '.txt':
            if file.size > 100 * 1024:
                raise serializers.ValidationError('Text file too large (max 100kb).')
            return file
        else:
            raise serializers.ValidationError('Unsupported file type')
