from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    """Serializer for creating and updating Book instances."""
    isbn = serializers.CharField(max_length=13, min_length=13)
    title = serializers.CharField(max_length=255)
    summary = serializers.CharField()
    language = serializers.CharField(max_length=2)
    publication_date = serializers.DateField()
    cover_url = serializers.CharField(allow_blank=True, required=False)
    pages = serializers.IntegerField()
    collection = serializers.UUIDField()

    authors = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        required=False,
    )
    genres = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        required=False,
    )
    publishers = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        required=False,
    )
    themes = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=True,
        required=False,
    )

    def validate_isbn(self, value):
        clean_isbn = value.replace('-', '').replace(' ', '')
        if len(clean_isbn) != 13 or not clean_isbn.isdigit():
            raise serializers.ValidationError("Invalid ISBN format, must be 13 digits.")
        return value
