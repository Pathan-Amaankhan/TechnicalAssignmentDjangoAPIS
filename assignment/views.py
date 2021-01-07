from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password

from assignment.models import Login, User


class LoginList(APIView):
    def get(self, request):
        login_details = Login.objects.filter(email=self.request.query_params.get('email'))
        return Response({
            'user_id': (list(login_details)[0].user_id if login_details else 'not registered'),
            'login_type': ('signin' if login_details else 'signup')
        })

    def post(self, request):
        parameters = self.request.data
        if 'email' in parameters:
            if 'password' in parameters and 'first_name' in parameters and 'last_name' in parameters:
                new_user = Login(email=parameters['email'], password=make_password(str(parameters['password'])),
                                 first_name=parameters['first_name'], last_name=parameters['last_name'])
                new_user.save()
                User(user_id=new_user.user_id, favourite="").save()
                response_string = 'registered Successfully'
            else:
                response_string = 'registration Unsuccessful missing required details'
            response = Response({
                'message': response_string
            })
        else:
            login_data = Login.objects.filter(user_id=self.request.data['user_id'])

            response = Response({
                'message': 'login successful' if
                'user_id' in parameters and 'password' in parameters
                and login_data
                and check_password(str(parameters['password']), list(login_data)[0].password) else 'failed'
            })

        return response


class UserList(APIView):
    def get(self, request):
        login_data = Login.objects.filter(user_id=self.request.query_params.get('user_id'))
        return Response({
            'email': list(login_data)[0].email,
            'first_name': list(login_data)[0].first_name,
            'last_name': list(login_data)[0].last_name,
            'favourites': list(User.objects.filter(user_id=self.request.query_params.get('user_id')))[0].favourite
        } if login_data else {'message': 'no user exists with id {}'.format(self.request.query_params.get('user_id'))})

    def post(self, request):
        parameters = self.request.data
        if 'to_delete' in parameters:
            favourite_data = User.objects.filter(user_id=parameters['user_id'])
            if str(parameters['to_delete']) == '0':
                if favourite_data:
                    list(favourite_data)[0].favourite += (str(parameters['category_name'])+',')
                    list(favourite_data)[0].save()
                    response = Response({'message': 'Added Successfully'})
                else:
                    response = Response({'message': 'no user exits with id {}'.format(parameters['user_id'])})
            else:
                if favourite_data and parameters['category_name'] in list(favourite_data)[0].favourite.split(','):
                    favourite_data = list(favourite_data)
                    temp = favourite_data[0].favourite.split(',')
                    temp.remove(parameters['category_name'])
                    favourite_data[0].favourite = ','.join(temp)
                    favourite_data[0].save()
                    response = Response({'message': 'removed successfully'})
                else:
                    response = Response({'message': 'The given category [{}] does not exists for current user'.format(parameters['category_name'])})

        else:
            response = Response({'message': 'missing required field to_delete'})

        return response
