Feature: Create Ticket from New

    Scenario Outline: Missing values in required fields
        Given user is logged into Manage
        When <Required Field> is blank
        Then display <Toolbar Error Title>
        And display <Toolbar Error Detail>
        And <UI Treatment>
        Examples:
            | Required Field    | Toolbar Error Title | Toolbar Error Detail    | UI Treatment
            | Summary            | Please correct the following issues on the following fields: | Summary is a required field | Outline the Summary label and value in red
            | Company | Please correct the following issues on the following fields:            | Company is a required field | Change the label text to red and the value focus to red