Feature: Create Ticket from New

    Scenario Outline: Missing values in required fields
        Given user is logged into Manage
        When <RequiredField> is blank
        Then display <ToolbarErrorTitle>
        Examples:
            | RequiredField    | ToolbarErrorTitle | ToolbarErrorDetail    | UITreatment  |
            | Summary            | Please correct the following issues on the following fields: | Summary is a required field | Outline the Summary label and value in red  |
            | Company | Please correct the following issues on the following fields:            | Company is a required field | Change the label text to red and the value focus to red |