import requests


def post_joke_image(
        token,
        owner_id,
        album_id,
        version_vk,
        image_file_name,
        message='',
):
    url = "https://api.vk.com/method/photos.getUploadServer"
    response_from_getUploadServer = requests.post(
        url=url,
        params={
            'access_token': token,
            'group_id': owner_id,
            'v': version_vk,
            'album_id': album_id,
        }
    )

    url = response_from_getUploadServer.json()['response']['upload_url']
    json_response_from_UploadServer = requests.post(
        url=url,
        files={
            'file1': (
                image_file_name,
                open(image_file_name, 'rb'),
                'multipart/form-data',
            )
        }
    ).json()

    url = "https://api.vk.com/method/photos.save"
    response_from_photos_save = requests.post(
        url=url,
        params={
            'access_token': token,
            'v': version_vk,
            'album_id': album_id,
            'group_id': owner_id,
            'server': json_response_from_UploadServer['server'],
            'photos_list': json_response_from_UploadServer['photos_list'],
            'hash': json_response_from_UploadServer['hash'],
        }
    )

    url = "https://api.vk.com/method/wall.post"
    response_from_wall_post = requests.post(
        url=url,
        params={
            'access_token': token,
            'from_group': 1,
            'owner_id': -owner_id,
            'message': message,  # Добавление текста поста
            'attachments': f'photo{-owner_id}_{response_from_photos_save.json()["response"][0]["id"]}',
            'v': version_vk,
        }
    )

    print(response_from_wall_post.json())


def post_custom_image(
        token,
        owner_id,
        album_id,
        version_vk,
        image_file_path,
        message=''
):
    url = "https://api.vk.com/method/photos.getUploadServer"
    response_from_getUploadServer = requests.post(
        url=url,
        params={
            'access_token': token,
            'group_id': owner_id,
            'v': version_vk,
            'album_id': album_id,
        }
    )

    upload_server_response = response_from_getUploadServer.json()
    if 'response' in upload_server_response:
        upload_url = upload_server_response['response']['upload_url']

        image_data = {
            'file1': (
                image_file_path,
                open(image_file_path, 'rb'),
                'multipart/form-data',
            )
        }

        json_response_from_UploadServer = requests.post(
            url=upload_url,
            files=image_data
        ).json()

        if 'response' in json_response_from_UploadServer:
            server = json_response_from_UploadServer['response']['server']
            photos_list = json_response_from_UploadServer['response']['photos_list']
            hash_value = json_response_from_UploadServer['response']['hash']

            url = "https://api.vk.com/method/photos.save"
            response_from_photos_save = requests.post(
                url=url,
                params={
                    'access_token': token,
                    'v': version_vk,
                    'album_id': album_id,
                    'group_id': owner_id,
                    'server': server,
                    'photos_list': photos_list,
                    'hash': hash_value,
                }
            )

            photos_save_response = response_from_photos_save.json()
            if 'response' in photos_save_response:
                photo_id = photos_save_response['response'][0]['id']

                url = "https://api.vk.com/method/wall.post"
                response_from_wall_post = requests.post(
                    url=url,
                    params={
                        'access_token': token,
                        'from_group': 1,
                        'owner_id': -owner_id,
                        'message': message,
                        'attachments': f'photo-{owner_id}_{photo_id}',
                        'v': version_vk,
                    }
                )

                print(response_from_wall_post.json())
            else:
                print("Ошибка при сохранении фотографии:", photos_save_response)
        else:
            print("Ошибка при загрузке фотографии на сервер VK:", json_response_from_UploadServer)
    else:
        print("Ошибка при получении upload_url:", upload_server_response)

# def post_custom_image(
#         token,
#         owner_id,
#         album_id,
#         version_vk,
#         image_file_path,
#         message=''
# ):
#     url = "https://api.vk.com/method/photos.getUploadServer"
#     response_from_getUploadServer = requests.post(
#         url=url,
#         params={
#             'access_token': token,
#             'group_id': owner_id,
#             'v': version_vk,
#             'album_id': album_id,
#         }
#     )
#
#     url = response_from_getUploadServer.json()['response']['upload_url']
#     json_response_from_UploadServer = requests.post(
#         url=url,
#         files={
#             'file1': (
#                 image_file_path,
#                 open(image_file_path, 'rb'),
#                 'multipart/form-data',
#             )
#         }
#     ).json()
#
#     url = "https://api.vk.com/method/photos.save"
#     response_from_photos_save = requests.post(
#         url=url,
#         params={
#             'access_token': token,
#             'v': version_vk,
#             'album_id': album_id,
#             'group_id': owner_id,
#             'server': json_response_from_UploadServer['server'],
#             'photos_list': json_response_from_UploadServer['photos_list'],
#             'hash': json_response_from_UploadServer['hash'],
#         }
#     )
#
#     url = "https://api.vk.com/method/wall.post"
#     response_from_wall_post = requests.post(
#         url=url,
#         params={
#             'access_token': token,
#             'from_group': 1,
#             'owner_id': -owner_id,
#             'message': message,  # Add post text
#             'attachments': f'photo{-owner_id}_{response_from_photos_save.json()["response"][0]["id"]}',
#             'v': version_vk,
#         }
#     )
#
#     print(response_from_wall_post.json())
