# Check Your Code Against the Following Points

## Don't forget to add `.gitignore` file BEFORE pushing

Make sure you don't push DB files (files with `.sqlite`, `.db3`, etc. extension).

Make sure you don't push `.pyc`, `.idea` files.


## Code Style

1. Make sure that your Response return status code:

Good example:

```python
if request.method == "GET":
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
```

Bad example:

```python
if request.method == "GET":
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

2. If you specify `max_length` then it's more reasonable 
to use `CharField` instead of `TextField`:

Good example:

```python
class Book(models.Model):
    description = models.CharField(max_length=255)
```

Bad example:

```python
class Book(models.Model):
    description = models.TextField(max_length=255)
```

3. Make sure that all your endpoint adds with `/`:

Good example:

```python
urlpatterns = [
    path("movies/<pk>/", movie_detail, name="config-detailed")
]
```

Bad example:

```python
urlpatterns = [
    path("movies/<pk>", movie_detail, name="config-detailed")
]
```

4. Make sure you catch an error in `@api_view` in case that object doesn't exist. 
Use `get_object_or_404` instead of `try`/`except` for this purpose.

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
