@e2e
Feature: Items Feature

  In order to manage my items stock
  As an authenticated user
  I would like to be able to have access to a list of all the items in my stock,
  be able to insert new item, edit existing item and delete existing item


Background:
  Given that I am in items page

  @items
  Scenario Outline: New Item
    When I click on New Item
    And fill new item Name as "<name>"
    And fill new item Height as "<height>"
    And fill new item Width as "<width>"
    And fill new item Weight as "<weight>"
    And I click on  Create Item
    Then I see the item in items list "<name>""<height>""<width>""<weight>"
    Examples:
      | name      | height    | width    | weight      |
      | DS-Item_1 | 10.5      | 2.1      | 100.0       |

  @items
  Scenario Outline: Edit Item
    When I click on "<old_name>" to show the item data
    And I click to edit the item
    And fill new item Name as "<name>"
    And fill new item Height as "<height>"
    And fill new item Width as "<width>"
    And fill new item Weight as "<weight>"
    And I click on  Create Item
    Then I see the item in items list "<name>""<height>""<width>""<weight>"
    Examples:
      | old_name | name       | height | width | weight |
      |DS-Item_1 | New-Item_1 | 5.5    | 3.0   | 99.9   |

  @items
  Scenario: Delete Item
    When I click on "DS-Item_1" to show the item data
    And I click to destroy the item
    Then I do not see "New-DS-Depo1" item in items list
