from behave import given, when, then

@given(u'user is logged into Manage')
def step_impl_login(context):
    print('DO LOGIN HERE')

@when(u'{RequiredField} is blank')
def step_impl_req_field(context, RequiredField):
    print('REQ FIELD IS BLANK {}'.format(RequiredField))

@then(u'display {ToolbarErrorDetail}')
def step_impl_error_detail(context, ToolbarErrorDetail):
    print('Error Detail is{}'.format(ToolbarErrorDetail))
#
# @then(u'display "{ToolbarErrorTitle}"')
# def step_impl_dashboard_status(context, row):
#   print('Dashboard Status for row {}'.format(row))
# @then(u'Clicking on Status Refresh should refresh status component')
# def step_impl_status_refresh(context):
#   print('Status Refresh button')
# @then(u'Dashboard Battery shows Battery or AC Power with correct icon.')
# def step_impl_battery_status(context):
#   print('Dashboard battery status')
# @then(u'Clicking on Battery Refresh should refresh battery component')
# def step_impl_battery_refresh(context):
#   print('Battery refresh')
# @then(u'Dashboard Settings shows correct values for row "{row}"')
# def step_impl_settings(context, row):
#   print('Dashboard settings for {}'.format(row))
# @then(u'Dashboard GPS shows correct values for row "{row}"')
# def step_impl_gps_settings(context, row):
#   print('Dashboard GPS row: {}'.format(row))