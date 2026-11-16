*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input Credentials   ab   salasana123
    Output Should Contain  Invalid username


Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  abc!  salasana123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  uusi  ab1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  uusi  salasanat
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  IstuuPuussa!