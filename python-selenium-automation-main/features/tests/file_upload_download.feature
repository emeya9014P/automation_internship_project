Feature: File upload and download capabilities
#  Scenario: User can download a file successfully
#    Given Go to the Tutorialspoint site
#    When Click on Download button
#    Then Verify downloaded file in the downloads directory

  Scenario: User can upload a file successfully
    Given Go to the Tutorialspoint site
    When Upload file "sample.txt"
    Then Verify "sample.txt" file is uploaded