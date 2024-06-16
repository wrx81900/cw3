import requests

POSTS_URL = 'https://my-json-server.typicode.com/typicode/demo/posts'
COMMENTS_URL = 'https://my-json-server.typicode.com/typicode/demo/comments'
PROFILE_URL = 'https://my-json-server.typicode.com/typicode/demo/profile'


def can_index_posts_test():
    req = requests.get(POSTS_URL)
    _expect_status_code(req.status_code, 200)

    post = req.json()[0]
    _expect_key(post, 'id')
    _expect_value(post['id'], 1)
    _expect_key(post, 'title')
    _expect_value(post['title'], 'Post 1')
    _print_passed()


def can_index_comments_test():
    req = requests.get(COMMENTS_URL)
    _expect_status_code(req.status_code, 200)

    comment = req.json()[0]
    _expect_key(comment, 'id')
    _expect_value(comment['id'], 1)
    _expect_key(comment, 'body')
    _expect_value(comment['body'], 'some comment')
    _expect_key(comment, 'postId')
    _expect_value(comment['postId'], 1)
    _print_passed()


def can_show_profile_test():
    req = requests.get(PROFILE_URL)
    _expect_status_code(req.status_code, 200)

    profile = req.json()
    _expect_key(profile, 'name')
    _expect_value(profile['name'], 'typicode')
    _print_passed()


def _expect_status_code(status_code, expected_code):
    if status_code != expected_code:
        raise Exception(f'Wrong status code! Status code {status_code} is different than {expected_code}')


def _expect_key(dict, expected_key):
    if expected_key not in dict:
        raise Exception(f'Wrong key! Dictonary does not have key {expected_key}')


def _expect_value(value, expected_value):
    if value != expected_value:
        raise Exception(f'Wrong value! Value "{value}" is different than expected "{expected_value}"')


def _print_passed():
    print('TEST PASSED')


def _print_failed(msg):
    print(f'TEST FAILED: {msg}')


def main():
    try:
        can_index_posts_test()
    except Exception as err:
        _print_failed(err)

    try:
        can_index_comments_test()
    except Exception as err:
        _print_failed(err)

    try:
        can_show_profile_test()
    except Exception as err:
        _print_failed(err)


main()
