from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# from main.models import Article


@csrf_exempt
def save(request):
    if request.method == "POST":
        name = "Hola Mundo desde Django"

        return JsonResponse(
            {"status": "success", "name": name, "method": request.method}
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def getArticles(request):
    if request.method == "POST":

        return JsonResponse(
            {
                "status": "success",
                "accion": "getArticles",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def getArticle(request):
    if request.method == "POST":

        return JsonResponse(
            {
                "status": "success",
                "accion": "getArticle",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def delete(request):
    if request.method == "POST":

        return JsonResponse(
            {
                "status": "success",
                "accion": "Delete Article",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def getArticlesByUser(request):
    if request.method == "POST":

        return JsonResponse(
            {
                "status": "success",
                "accion": "getArticleByUser",
            }
        )

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
