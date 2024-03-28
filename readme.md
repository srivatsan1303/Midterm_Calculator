# Advanced Python Calculator with History Management

The Advanced Python Calculator is a comprehensive tool designed for performing arithmetic operations and meticulously tracking each calculation's history. With the integration of the Pandas library, this application not only executes basic arithmetic but also records every operation in a structured CSV file, facilitating easy access to past calculations. This guide outlines the setup, usage, and testing framework for the calculator, ensuring users can fully leverage its capabilities.

## Getting Started

### Installation

1. **Clone the Project Repository**
   #Begin by cloning the repository to your local machine using the command:

   git clone <repository_url>

2. **Install Dependencies**
   #Install the necessary Python packages listed in `requirements.txt`:

   pip install -r requirements.txt


3. **Environment Configuration**
   #Create a `.env` file in the root directory of the project and define the path for your calculation history file:

   CALCULATION_HISTORY_PATH = './data/calculation_history.csv'

4. **Run the Application**
   #Start the calculator application:

   python3 main.py

## Usage

Upon launching `main.py`, the application presents a CLI from which users can access various arithmetic operations and manage the calculation history.**menu** command is used to project the list of registered commands.

1.)Type any of the below commands in the REPL command interface
2.)Enter the numbers when asked 
3.)Interface computes and displays the result.

### Arithmetic Operations

- **Addition**: Input `add` followed by two numbers to calculate their sum.
- **Subtraction**: Use `subtract` for difference calculations.
- **Multiplication**: Invoke `multiply` to product two numbers.
- **Division**: Use `divide` for division, with built-in handling for division by zero.

### History Management

- **Load**:Review your calculation log with `load`, which outputs a table that summarizes the history of calculations, as shown below:.

data history of calculator:
ID  | action | value1 | value2 | result
----|--------|--------|--------|-------
1   | mul    | 3.0    | 2.0    | 6.0
2   | div    | 6.0    | 2.0    | 3.0
3   | div    | 6.0    | 0.0    | Error

- **Clear**: Erase the calculation history using `clear`.
- **Delete**: Remove specific entries from the history with `delete`.

## Design Patterns and Architecture

### Simplification through Abstraction: History Management
- **Facade Pattern**: Central to our system's interaction with data storage, the CalculationHistory class embodies the Facade Pattern. It simplifies the complexities involved in CSV manipulation using pandas, offering methods like log_data, fetch_as_list, fetch_as_data_frame, and clear. These interfaces allow for easy data operations without delving into the specifics of pandas or direct file manipulation.[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/history/__init__.py)

### Structured Commands: Operational Encapsulation
- **Command Pattern**: The essence of our operation execution lies within the execute method. This approach conceptualizes each operation — be it add, sub, and beyond — as distinct objects that encapsulate specific functionalities, streamlining the execution process.[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/plugins/add/__init__.py)

### Dynamic Expansion: Plugin Integration
- **Factory Method Pattern**:  Our system's capability to seamlessly introduce new functionalities is showcased through the load_plugin method. This method exemplifies the Factory Method Pattern, dynamically incorporating additional plugins without the need for manual configuration adjustments.
[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/__init__.py)

### Uniqueness in Instance Management: Menu Command
- **Singleton Pattern**: The MenuCommand stands as a testament to the Singleton Pattern, ensuring a single, unified instance exists across the application lifecycle, thereby optimizing resource utilization and consistency.[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/__init__.py)

## Logging and Error Handling

### Initial Setup
- **Logging**: The application employs Python's built-in logging library to monitor actions and identify discrepancies.Upon launch, our logging framework is primed, setting the stage for detailed observance throughout the application lifecycle. This is achieved by configuring log levels, formats, and, if necessary, output destinations, ensuring a tailored logging experience[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/logging.conf)

### Operational Logging
- **Error Handling**: As users interact with the application, every action, anomaly, or error is logged, offering real-time insights into application health and user engagement patterns. This proactive logging strategy extends from user operations to system-level events, such as file directory creation or access issues.It is used in the start function in this below code.[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/__init__.py)

## EAFP (Easier to Ask for Forgiveness than Permission):

### Exception Management
Adhering to the principle of EAFP, our system is designed to optimistically execute operations while being fully prepared to handle exceptions gracefully. This approach not only enhances code readability but also ensures robust error handling across the application.The ZeroDivisionError is an exception that has been handled in this below code[link](https://github.com/srivatsan1303/Midterm_Calculator/blob/main/app/plugins/divide/__init__.py)

## Testing Framework

This application includes a suite of tests to ensure reliability and accuracy. Utilizing pytest, tests cover various scenarios including basic operations, handling unknown commands, and managing calculation history.

### Running Tests

Execute the test suite using pytest:

pytest 

Test cases include:
- Environment variable retrieval.
- Exit command execution.
- Handling of unknown commands.
- Arithmetic operations: add, subtract, multiply, and divide.
- Division by zero handling.
- History management commands: fetch, delete, and clear.

## Contributions

Contributions are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, feel free to fork the repository and submit a pull request.


This README provides a comprehensive overview of the Advanced Python Calculator, from setup and usage to testing and contributing. By following this guide, users can effectively navigate the application, leveraging its full range of functionalities.

