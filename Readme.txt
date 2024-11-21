Django superuser:

username: admindjango
password: employee@123!

Endpoints available:

•Template render:

    /restaurant/

•API calls:

    /restaurant/api/booking/
    /restaurant/api/menu/

•Generate token(via DRF):
    POST /restaurant/api-token-auth/

•Djoser endpoints:

    POST /auth/users/
    GET /auth/users/
    GET /auth/users/{id}/
    PUT /auth/users/{id}/
    DELETE /auth/users/{id}/
    POST auth/users/login/