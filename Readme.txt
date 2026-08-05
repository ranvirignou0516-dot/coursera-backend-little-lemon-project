Little Lemon Web Application Backend API

Authentication
POST /auth/token/login/
GET /auth/users/me/

Menu APIs
GET /restaurant/menu/
GET /restaurant/menu/<id>/
POST /restaurant/menu/
PUT /restaurant/menu/<id>/
PATCH /restaurant/menu/<id>/
DELETE /restaurant/menu/<id>/

Booking APIs
GET /restaurant/booking/
GET /restaurant/booking/<id>/
POST /restaurant/booking/
PUT /restaurant/booking/<id>/
PATCH /restaurant/booking/<id>/
DELETE /restaurant/booking/<id>/

Authentication Header

Authorization: Token <your_token>