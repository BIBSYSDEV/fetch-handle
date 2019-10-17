# Fetch handle

This service *should* fetch a Handle, however as there is no service to fetch a Handle from, then this is a bit difficult, so the function currently returns a UUID.

# TODO

  - Functionality
    - The service takes a resource URL
    - Identify a handle service that will provide a Handle.
  
  - Lifecycle
    - Testing
      - Unit tests
      - Integration tests
        - How is this done?
    - Set up PEP8 check
    - Set up CI/CD
      - Checks
        - Static analysis
          - Code style
          - Coverage (100%)
    - Fix naming conventions
      - How are variables named in Python?
      - Rename Function in SAM, other places

#### Testing locally
     
##### Install python requirements locally (necessary for running unittests in command line)
`project-directory$ pip3 install -r src/requirements.txt`
  
##### Run tests
`project-directory$ python3 -m unittest discover test`    
  
##### Invoke lambda locally
`project-directory$ sam build`
`project-directory$ sam local invoke FetchHandle -e event.json`

##### Start local lambda service
`project-directory$ sam local start-lambda`
  
##### Start api locally
`project-directory$ sam local start-api`

#### Other sam local command examples
  
##### Package (for deploy or publishing)  
`project-directory/.aws-sam/build$ sam package --template-file ./template.yaml --s3-bucket [EXISTING_BUCKET_NAME] --output-template-file packaged.yaml`
  
##### Deploy package
`project-directory/.aws-sam/build$ sam deploy --template-file ./packaged.yaml --stack-name [CREATE_A_STACK_NAME] --capabilities CAPABILITY_NAMED_IAM`
  
##### Publish package
`project-directory/.aws-sam/build$ sam package --template-file ./packaged.yaml --region eu-west-1`
