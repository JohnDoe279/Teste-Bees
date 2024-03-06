@e2e
Feature: Deposits Feature

  In order to manage my deposits
  As an authenticated user
  I would like to be able to have access to a list of all the deposits,
  be able to create new deposit, edit existing deposit and delete existing deposit


Background:
  Given that I am in deposits page

  @deposits
  Scenario Outline: New Deposit
    When I click on New Deposit
    And fill new deposit Name as "<name>"
    And fill new deposit Address as "<address>"
    And fill new deposit City as "<city>"
    And fill new deposit State as "<state>"
    And fill new deposit Zipcode as "<zipcode>"
    And I click on  Create Deposit
    Then I see the deposit in deposits list "<name>""<address>""<city>""<state>""<zipcode>"
    Examples:
      | name     | address        | city       | state    | zipcode   |
      | DS-Depo1 | DS Test Street | Klapaucius | DS       | 08125-874 |

  @deposits
  Scenario Outline: Edit Deposit
    When I click on "<old_name>" to show the deposit data
    And I click to edit the deposit
    And fill new deposit Name as "<name>"
    And fill new deposit Address as "<address>"
    And fill new deposit City as "<city>"
    And fill new deposit State as "<state>"
    And fill new deposit Zipcode as "<zipcode>"
    And I click on Update Deposit
    Then I see the deposit in deposits list "<name>""<address>""<city>""<state>""<zipcode>"
    Examples:
      | old_name | name         | address            | city            | state  | zipcode   |
      |DS-Depo1  | New-DS-Depo1 | New DS Test Street | New Klapaucius  | New DS | 54678-123 |

  @deposits
  Scenario: Delete Deposit
    When I click on "New-DS-Depo1" to show the deposit data
    And I click to destroy the deposit
    Then I do not see "New-DS-Depo1" deposit in deposits list
