from rest_framework.filters import BaseFilterBackend
import coreapi

'''
Helper class for sending string parameters through the Swagger UI interface
'''


# TODO: Make function for dynamic fields creation
# TODO: Find some way to replace field's type and description


class TransactionFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='transaction_type',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
            name='order_by',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
            name='from_date',
            description='inclusive',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
            name='to_date',
            description='inclusive',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
            name='specific_user',
            location='query',
            required=False,
            type='string'
        ), coreapi.Field(
            name='specific_date',
            description='exact day',
            location='query',
            required=False,
            type='string'
        ),

        ]
