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