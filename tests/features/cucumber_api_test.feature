Feature: Api

  Scenario: to verify the api
    Given API request
    When request is equal to "2"

  Scenario Outline: the api
    Given number one "<initial>"
    When request add "<some>"
    Then total add "<sum_total>"

    Examples: Amounts
      | initial | some | sum_total |
      | 2       | 4    | 6     |
      | 0       | 0    | 0     |
      | 1       | 1    | 2     |