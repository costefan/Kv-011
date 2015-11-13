from behave import given, when, then


def eq(a, b, msg='{a} != {b}'):
    if a != b:
        raise AssertionError(msg.format(a=a, b=b))


@then(u'I should see "{url}"')
def i_should_see(context, url):
    path_info = context.browser.url
    eq(path_info, url)
    assert path_info == url


@when(r'I visit url "{url}"')
def i_visit_url(context, url):
    br = context.browser
    br.visit(url)


@given('a user')
def step_impl(context):
    from django.contrib.auth.models import User
    u = User(username='foo', email='foo@example.com')
    u.set_password('bar')


@when('I log in')
def step_impl(context):
    br = context.browser
    br.visit('http://localhost:8081/auth/login/')
    br.find_by_css('#username').first.fill('Nt')
    br.find_by_css('#password').first.fill('111111')
    br.find_by_value('Log in').first.click()


@then('I see index page')
def step_impl(context):
    br = context.browser
    assert br.url


@when('I gave not valid data')
def step_impl(context):
    br = context.browser
    br.visit('http://localhost:8081/auth/login/')
    br.find_by_css('#username').first.fill('User1')
    br.find_by_css('#password').first.fill('111111')
    br.find_by_value('Log in').first.click()


@then('I see login form and see error message')
def step_impl(context):
    br = context.browser
    eq(br.url, 'http://localhost:8081/auth/login/')
    assert br.url == 'http://localhost:8081/auth/login/'
    assert context.browser.is_element_present_by_css('.error')


# TODO:
# Invalid email or password add