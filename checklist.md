# Check Your Code Against the Following Points

## Don't forget to add `.gitignore` file BEFORE pushing

Make sure you don't push DB files (files with `.sqlite`, `.db3`, etc. extension).

Make sure you don't push `.pyc`, `.idea` files.


## Code Style

1. Make sure that your `Response` returns status code:

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

3. Make sure that all your endpoints end with `/`:

Good example:

```python
urlpatterns = [
    path("movies/<pk>/", movie_detail, name="project-detailed")
]
```

Bad example:

```python
urlpatterns = [
    path("movies/<pk>", movie_detail, name="project-detailed")
]
```

4. Make sure you catch an error in `@api_view` in case that object doesn't exist. 
Use `get_object_or_404` instead of `try`/`except` for this purpose.

5. Make sure you've added a blank line at the end of all your files.
6. A serializer field is required by default. ([DRF required documentation](https://www.django-rest-framework.org/api-guide/fields/#required))
7. Your project should be one-styled, don't use double and single quotes at the same time. Double quotes are preferred.

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
