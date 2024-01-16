from rest_framework.views import APIView, status, Request, Response
from accounts.models import Account
from django.forms import model_to_dict
from django.db import IntegrityError


# class AccountView that extends APIView CRUD methods, and others
class AccountView(APIView):
    # get method that returns all accounts
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()
        converted_accounts = []
        for account in accounts:
            converted_account = model_to_dict(account)
            converted_accounts.append(converted_account)
        return Response(converted_accounts, status=status.HTTP_200_OK)
        # accounts = Account.objects.all()
        # serializer = AccountSerializer(accounts, many=True)
        # return Response(serializer.data)

    # post method that creates an account
    def post(self, request: Request) -> Response:
        user_data = request.data
        try:
            account = Account.objects.create(**user_data)
        except IntegrityError as ie:
            return Response(
                "CPF already in used account", status=status.HTTP_400_BAD_REQUEST
            )
        converted_account = model_to_dict(account)
        return Response(converted_account, status=status.HTTP_201_CREATED)

        # serializer = AccountSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # # if serializer is not valid, return error
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    # get method that returns an account by id
    def get(self, request: Request, account_id: int) -> Response:
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist as e:
            return Response("Account not found", status=status.HTTP_404_NOT_FOUND)
        converted_account = model_to_dict(account)
        return Response(converted_account, status=status.HTTP_200_OK)

        # try:
        #     account = Account.objects.get(pk=pk)
        # except Account.DoesNotExist as e:
        #     return Response("Account not found", status=status.HTTP_404_NOT_FOUND)
        # serializer = AccountSerializer(account)
        # return Response(serializer.data)

    # put method that updates an account by id
    def put(self, request: Request, account_id: int) -> Response:
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist as e:
            return Response("Account not found", status=status.HTTP_404_NOT_FOUND)
        user_data = request.data
        account.name = user_data.get("name", account.name)
        account.cpf = user_data.get("cpf", account.cpf)
        account.balance = user_data.get("balance", account.balance)
        account.save()
        converted_account = model_to_dict(account)
        return Response(converted_account, status=status.HTTP_200_OK)

        # try:
        #     account = Account.objects.get(pk=pk)
        # except Account.DoesNotExist as e:
        #     return Response("Account not found", status=status.HTTP_404_NOT_FOUND)
        # serializer = AccountSerializer(account, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # # if serializer is not valid, return error
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete method that deletes an account by id
    def delete(self, request: Request, account_id: int) -> Response:
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist as e:
            return Response("Account not found", status=status.HTTP_404_NOT_FOUND)
        account.delete()
        return Response("Account deleted", status=status.HTTP_204_NO_CONTENT)

        # try:
        #     account = Account.objects.get(pk=pk)
        # except Account.DoesNotExist as e:
        #     return Response("Account not found
