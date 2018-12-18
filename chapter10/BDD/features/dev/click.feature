Feature:

  Scenario Outline: 点击贴吧

    Given 首页

    When 点击贴吧
    Then 返回数据

    When 搜索贴吧<term>
    Then 返回数据<result>

  Examples: 数据
    |term     | result  |
    |LilyLove | 1       |
    |Lily     | 1       |

