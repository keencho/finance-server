import typing


def build_success_response(data: typing.Any):
    return {'success': True, 'data': data}