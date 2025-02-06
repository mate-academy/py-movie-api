import pytest
from django.urls import reverse
from cinema.models import Movie


@pytest.fixture(scope="module")
def movie_list_url():
    return reverse("cinema:movie-list")


@pytest.fixture(scope="function")
def single_movie_url():
    def _movie_url(pk):
        return reverse("cinema:movie-detail", kwargs={"pk": pk})

    return _movie_url


@pytest.fixture(scope="function")
def create_movies():
    for i in range(1, 4):
        Movie.objects.create(title=f"Title {i}", description=f"Desc {i}", duration=i)


@pytest.mark.django_db
def test_movie_list_get(client, movie_list_url, create_movies):
    movies = Movie.objects.all()

    response = client.get(movie_list_url)

    assert response.status_code == 200
    assert len(response.data) == len(movies)

    for movie_obj, movie_data in zip(movies, response.data):
        assert movie_data["title"] == movie_obj.title
        assert movie_data["description"] == movie_obj.description
        assert movie_data["duration"] == movie_obj.duration


@pytest.mark.django_db
def test_movie_list_post_one_movie(client, movie_list_url):
    data = {
        "title": "New Movie",
        "description": "New Movie Description",
        "duration": 120,
    }
    response = client.post(movie_list_url, data, format="json")

    assert response.status_code == 201
    assert response.data["title"] == data["title"]
    assert Movie.objects.filter(title="New Movie").exists()


@pytest.mark.django_db
def test_movie_list_post_two_movies(client, movie_list_url):
    data = [
        {"title": "test 1", "description": "desc 1", "duration": 100},
        {"title": "test 2", "description": "desc 2", "duration": 200},
    ]
    response = client.post(movie_list_url, data, content_type="application/json")

    assert response.status_code == 201
    assert len(response.data) == 2
    assert Movie.objects.filter(title="test 1").exists()
    assert Movie.objects.filter(title="test 2").exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "movie_id, expected_title",
    [
        (1, "Title 1"),
        (2, "Title 2"),
        (3, "Title 3"),
    ],
)
def test_movie_detail_get(
    client, single_movie_url, create_movies, movie_id, expected_title
):
    response = client.get(single_movie_url(pk=movie_id))

    assert response.status_code == 200
    assert response.data["title"] == expected_title


@pytest.mark.django_db
@pytest.mark.parametrize(
    "movie_id, expected_title",
    [
        (1, "New Title 1"),
        (2, "New Title 2"),
        (3, "New Title 3"),
    ],
)
def test_movie_detail_put(
    client, single_movie_url, create_movies, movie_id, expected_title
):
    movie = Movie.objects.get(id=movie_id)

    data = {
        "title": f"New Title {movie_id}",
        "description": movie.description,
        "duration": movie.duration,
    }

    response = client.put(
        single_movie_url(pk=movie_id), data, content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data["title"] == expected_title


@pytest.mark.django_db
@pytest.mark.parametrize("movie_id", (1, 2, 3))
def test_movie_detail_delete(client, single_movie_url, create_movies, movie_id):
    response = client.delete(
        single_movie_url(pk=movie_id), content_type="application/json"
    )

    assert response.status_code == 204
    assert Movie.objects.filter(id=movie_id).exists() == False
