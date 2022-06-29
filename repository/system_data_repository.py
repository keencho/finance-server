from model import SystemData

model = SystemData


def save_or_update(key: str, value: str):

    exist_data = model.filter(model.key == key).first()

    if exist_data is None:
        data = model(
            key=key,
            value=value
        )
        data.save()
    else:
        exist_data.value = value
        exist_data.save()