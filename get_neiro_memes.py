# import openai
# import json
#
# api_key = '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'
#
#
# def get_neiro_memes():
#     openai.api_key = api_key
#     img = openai.Image.create(
#         prompt='dog and cat memes',
#         n=10,
#         size='512x512',
#         response_format='url'
#     )
#     image = {'img': []}
#     for url in img['data']:
#         image['img'].append(url['url'])
#
#     with open('neiro.json', 'w') as file:
#         json.dump(image, file)