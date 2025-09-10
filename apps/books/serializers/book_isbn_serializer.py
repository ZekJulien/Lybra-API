from rest_framework import serializers

class IsbnSerializer(serializers.Serializer):
    """Serializer for validating ISBN input."""
    isbn = serializers.CharField(max_length=17)

    def validate_isbn(self, value):
        clean_isbn = value.replace('-', '').replace(' ', '')
        if len(clean_isbn) != 13 or not clean_isbn.isdigit():
            raise serializers.ValidationError("Invalid ISBN format, must be 13 digits.")
        return value
