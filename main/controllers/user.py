from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import User
from main.serializers import UserSerializer
from main.validator import UserValidatorForm


@csrf_exempt
def save(request):
    if request.method == "POST":

        # Obtenemos la contraseña del usuario y la ciframos
        password = request.POST.get("password", False)
        passwordEncoded = make_password(password)

        # Validar los datos del usuario
        form = UserValidatorForm(request.POST)

        if form.is_valid():
            # Crear un objeto de usuario
            user_data = User(
                name=request.POST.get("name"),
                surname=request.POST.get("surname"),
                nick=request.POST.get("nick").lower(),
                email=request.POST.get("email").lower(),
                bio=request.POST.get("bio", False),
                password=passwordEncoded,
            )

        else:
            return JsonResponse(
                {"error": "Invalid data", "details": form.errors}, status=400
            )

        # Comprobar si el usuario no existe en la base de datos
        try:
            usersFinds = User.objects.filter(
                Q(email=user_data.email.lower()) | Q(nick=user_data.nick.lower())
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

        # Si se encuentra, devolver un error
        if len(usersFinds) > 0:
            return JsonResponse({"error": "User already exists"}, status=400)
        else:

            # Guardar el usuario en la base de datos
            user_data.save()

            # Devolver una respuesta de éxito
            userSz = UserSerializer(user_data, many=False)

            return JsonResponse({"status": "success", "user": userSz.data})

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def login(request):
    # Comprobar el metodo http que me llega
    if request.method == "POST":

        # Verificar si llegan los datos para el login
        if (
            request.POST
            and request.POST.get("email", False)
            and request.POST.get("password", False)
        ):
            # Sacar los valores del email y la contraseña
            email = request.POST.get("email").lower()
            password = request.POST.get("password")

            # Buscar usuario con el correo recibido
            userLogin = User.objects.filter(email=email).first()

            # Sacar contraseña cifrada
            passwordEncoded = userLogin.password

            # Verificar la contraseña para ver si coincide
            if check_password(password, passwordEncoded):
                # Serializar usuario para devolver un json luego
                userLoginSerializer = UserSerializer(userLogin)
                userLoginData = userLoginSerializer.data

                # Generar token JWT

                # Devolver respuesta positiva con el usuario y el token
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)

        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

        return JsonResponse(
            {
                "status": "success",
                "accion": "login",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def profile(request):
    if request.method == "POST":

        return JsonResponse(
            {
                "status": "success",
                "accion": "Profile",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
