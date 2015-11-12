# Created by costefan at 12.11.15
Feature: Login for site

  Scenario: Show login form
    Given a user
    When I visit url "http://localhost:8081"
    Then I should see "http://localhost:8081/login/?next=/"

  Scenario: Logging in to our system
    Given a user
    When I log in
    Then I see index page

  Scenario: Logging with wrong data
    Given a user
    When I gave not valid data
    Then I see login form and see error message
