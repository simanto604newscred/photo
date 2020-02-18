from django.urls import reverse


class TestObtainToken:
    url = reverse('token:obtain')
    password = 'password'

    def test_get_token(self, client, user):
        user.set_password(self.password)
        user.save()

        data = {
            'username': user.username,
            'password': self.password
        }

        response = client.post(self.url, data=data)

        assert response.status_code == 200
        assert response.data.get('access', '')
        assert response.data.get('refresh', '')

    def test_error_on_incorrect_credentials(self, client, user):
        data = {
            'username': user.username,
            'password': self.password
        }

        response = client.post(self.url, data=data)

        assert response.status_code == 401
        assert response.data.get('detail', '') == 'No active account found with the given credentials'
