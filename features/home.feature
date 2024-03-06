@e2e
Feature: Home Feature

  As an authenticated user
  I would like to have access to deposits, items and inventory screen located in my home page
  To be able manage and plan future actions

Background:
  Given that I am in home page

@home
 Scenario Outline: Home pages availability
    When I click on "<page>"
    Then "<page>" page is displayed
    Examples:
     | page |
     |Deposits|
     |Items   |
     |Inventory|