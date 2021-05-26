from rest_framework.filters import BaseFilterBackend
import coreapi


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
            name='user_id',
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
            name='date',
            description='exact day',
            location='query',
            required=False,
            type='string'
        ),

        ]
