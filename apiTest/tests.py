from ApiTask.apiData.NewRpaApiData.new_rpa_api_data import Rpa_api
from assertpy import assert_that


api_test = Rpa_api()

#setting access token

api_test.set_access_token(api_test.acces_token(api_test.get_rpa_fqdn()))

#executing get trigger api request
api_test.get_triggers(api_test.get_access_token(), api_test.get_rpa_fqdn())
assert_that(api_test.get_triggers(api_test.get_access_token(), api_test.get_rpa_fqdn()).status_code).is_equal_to(200)



print(api_test.get_rpa_fqdn())
print(api_test.get_access_token())
print(api_test.get_triggers(api_test.get_access_token(), api_test.get_rpa_fqdn()).json())