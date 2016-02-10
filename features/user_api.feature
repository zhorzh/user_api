Feature: user API
	Scenario: create user
		When POST user
		Then response status code is 200
		And response contains JWT

    Scenario: register user with email and password
        Given valid user
		When POST user
        And register user with email and password
		Then response status code is 200
		And response contains JWT
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

    Scenario: authenticate user with email only
        Given invalid user with email only
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 422

    Scenario: authenticate user with password only
        Given invalid user with password only
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 422

    Scenario: authenticate user with wrong password
        Given invalid user with wrong password
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 404

    Scenario: authenticate user with wrong email
        Given invalid user with wrong email
		When POST user
        And register user with email and password
        And authenticate user with email and password
		Then response status code is 404

    Scenario: update user email
        Given valid email
        Given valid user
		When POST user
        And register user with email and password
        And update user email
		Then response status code is 200
		And response contains user
        And user email is updated

    Scenario: update user password
        Given valid password
        Given valid user
		When POST user
        And register user with email and password
        And update user password
		Then response status code is 200
		And response contains user
        And user password is updated
