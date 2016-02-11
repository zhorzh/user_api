Feature: user API
	Scenario: create user
		When POST user
		Then response status code is 200
		And response contains JWT
        And response token scope is anonymous

    Scenario: register user with email and password
        Given valid user
		When POST user
        And register user with email and password
		Then response status code is 200
		And response contains user

    Scenario: register user with email only
        Given invalid user with email only
		When POST user
        And register user with email and password
		Then response status code is 422
		And response not contains JWT

    Scenario: register user with password only
        Given invalid user with password only
		When POST user
        And register user with email and password
		Then response status code is 422
		And response not contains JWT

    Scenario: authenticate user with email and password
        Given valid user
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 200
		And response contains JWT
        And response token scope is authenticated

    Scenario: authenticate user with email only
        Given invalid user with email only
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 422
		And response not contains JWT

    Scenario: authenticate user with password only
        Given invalid user with password only
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 422
		And response not contains JWT

    Scenario: authenticate user with wrong password
        Given valid user
        Given invalid user with wrong password
		When POST user
        And register user with email and password
        And authenticate invalid user with email and password
		Then response status code is 404
		And response not contains JWT

    Scenario: authenticate user with wrong email
        Given valid user
        Given invalid user with wrong email
		When POST user
        And register user with email and password
        And authenticate invalid user with email and password
		Then response status code is 404
		And response not contains JWT

    Scenario: update user email
        Given valid email
        Given valid user
		When POST user
        And register user with email and password
        And authenticate user with email and password
        And update user email
		Then response status code is 200
		And response contains user
        And user email is updated
        And response token scope is authenticated

    Scenario: update user password
        Given valid password
        Given valid user
		When POST user
        And register user with email and password
        And authenticate user with email and password
        And update user password
        And unauthenticate user with email and password
        And authenticate user with email and password
		Then response status code is 200
		And response contains user
		And response contains JWT
        And response token scope is authenticated
