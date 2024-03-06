@e2e
Feature: Login Feature

Background:
  Given that I am in login page

  @login
  Scenario: Sign up new user
    When I click on Sign up button
    And fill the sign up form
    And click on Sign up button
    Then the new user is registered

  @login
  Scenario: Login with valid credentials
    When I enter my credential and submit
    Then i am logged in