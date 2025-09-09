from typing import TypeVar, Generic, Optional, List, Dict, Any
from django.db.models import Model

T = TypeVar('T', bound=Model)

class BaseService(Generic[T]):
    """
    Generic base service providing standard CRUD operations for Django models.
    This class is meant to be extended with a specific model.
    """

    model: type[T] = None

    @classmethod
    def get(cls, pk: Any) -> T:
        """
        Retrieve an instance by primary key.

        Args:
            pk (Any): The primary key of the instance.

        Returns:
            T: The model instance.

        Raises:
            django.core.exceptions.ObjectDoesNotExist: If no instance matches the query.
        """
        return cls.model.objects.get(pk=pk)

    @classmethod
    def list(cls, filters: Optional[Dict[str, Any]] = None) -> List[T]:
        """
        List instances, optionally filtered by given keyword arguments.

        Args:
            filters (Optional[Dict[str, Any]]): Filter conditions as field lookup keyword arguments.

        Returns:
            List[T]: A list of model instances.
        """
        qs = cls.model.objects.all()
        if filters:
            qs = qs.filter(**filters)
        return list(qs)

    @classmethod
    def create(cls, **data) -> T:
        """
        Create a new instance with the provided data.

        Args:
            **data: Field values for the new instance.

        Returns:
            T: The created model instance.
        """
        return cls.model.objects.create(**data)

    @classmethod
    def update(cls, pk: Any, **data) -> T:
        """
        Update an existing instance identified by primary key with provided data.

        Args:
            pk (Any): Primary key of the instance to update.
            **data: Fields and values to update. Fields with None values are ignored.

        Returns:
            T: The updated model instance.

        Raises:
            django.core.exceptions.ObjectDoesNotExist: If instance does not exist.
        """
        instance = cls.get(pk)
        for attr, value in data.items():
            if value is not None:
                setattr(instance, attr, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, pk: Any) -> None:
        """
        Delete an instance by primary key.

        Args:
            pk (Any): Primary key of the instance to delete.

        Raises:
            django.core.exceptions.ObjectDoesNotExist: If instance does not exist.
        """
        instance = cls.get(pk)
        instance.delete()
