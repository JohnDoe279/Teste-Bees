# Bees Test Challenge

## Description
The objective of this automation project is to automate following:

Website: https://test-bees.herokuapp.com/

API: https://swapi.dev/ 

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package manager)

### Installing Dependencies
You can install the project dependencies by running the following command:
```bash
pip install -r requirements.txt
```

Make sure you are in the root of your project, where the `requirements.txt` file is located.

### Dependencies
- allure_python_commons==2.13.2
- behave==1.2.6
- selenium==4.18.1
- selenium_page_factory==2.6
- Faker~=23.3.0
- requests~=2.31.0

### Executing the Project
You can execute the project by running the following command:
```bash
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
``` 
To execute only API tests
```bash
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features --tags=@api
``` 
To execute only E2E tests
```bash
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features --tags=@e2e
``` 
For specific test suit execution, please include the tag of the suit in the command line
```bash
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features --tags={add_tag_here}
``` 

### Generating the Report
After executing the project, you can generate the Allure report by running the following command:
```bash
allure serve %allure_result_folder%
``` 

Make sure you have Allure installed on your system. You can install it using the following command:
```bash
npm install -g allure-commandline
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
