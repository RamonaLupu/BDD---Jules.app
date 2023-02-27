Feature: Test the Jules page

  Background:
    Given Home page: Open jules.app

  @Test1
  Scenario: Check the error message when i leave the pass field empty
    When Home page: Input correct email
    When Home page: Leave pass empty
    Then Home page: Verify error ‘Please enter your password!’ is displayed
    Then Home page: Verify Log in btn is disabled

  @Test2
  Scenario: Verify URL
    When Home page: Click on Sign up
    Then Sing-up page: Verify the excepted_url "https://jules.app/sign-up"
    When Sing-up page: Click on Log in
    Then Home page: Verify the expected_url "https://jules.app/sign-in"

  @Test3
  Scenario: click on the sign_up and verify the error on the email textbox
    When Sign_in: I click on the sign_up button
    When Sign_up: I click personal radio button
    When Sign_up: I click continue button
    When Sign_up: I send first name "Ramona"
    When Sign_up: I click continue first name button
    When Sign_up: I send last name "Radu"
    When Sign_up: I click continue last name button
    When Sign_up: I set my email to "ramo"
    When Sign_up: I receive message: Please enter a valid email address
    When Sign_up: I clear the email textbox
    When Sign_up: I put the correct email
    Then Sign_up: I verify that error is not displayed anymore

  @Test4
  Scenario: Check the error message when I put the incorrect password
    When Home page: I input the correct email
    When Home page: I put the incorrect password
    Then Home page: Verify error ‘Invalid email/password combination’ is displayed
    Then Home page: Verify Log in btn is displayed




